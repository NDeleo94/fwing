from django.db.models import Q
from apps.fw.models.user_model import FwUser

from apps.fw.serializers.egresado_serializers import EgresadoUpdateSerializer

from apps.fw.utils.general_utils import title_case
from apps.fw.utils.ciudad_utils import get_or_create_ciudad
from apps.fw.utils.carrera_utils import check_carrera_following, get_carrera_following
from apps.fw.utils.egreso_utils import create_egreso
from apps.fw.utils.privacidad_utils import create_privacidad


def create_egresado(json_egresado):
    dni_egresado = int(json_egresado.get("nro_documento"))
    apellidos_egresado = title_case(json_egresado, "apellido")
    nombres_egresado = title_case(json_egresado, "nombres")
    email_egresado = json_egresado.get("email")
    fecha_nac_egresado = json_egresado.get("fecha_nacimiento")
    nacionalidad_egresado = title_case(json_egresado, "nacionalidad")
    sexo_egresado = title_case(json_egresado, "sexo")

    ciudad_natal_egresado = get_or_create_ciudad(
        title_case(json_egresado, "localidadnac")
    )
    ciudad_actual_egresado = get_or_create_ciudad(
        title_case(json_egresado, "localidad")
    )

    data_egresado = {
        "dni": dni_egresado,
        "apellidos": apellidos_egresado,
        "nombres": nombres_egresado,
        "email": email_egresado,
        "fecha_nac": fecha_nac_egresado,
        "nacionalidad": nacionalidad_egresado,
        "ciudad_natal": ciudad_natal_egresado.id,
        "ciudad_actual": ciudad_actual_egresado.id,
        "sexo": sexo_egresado,
    }
    serializer = EgresadoUpdateSerializer(data=data_egresado)
    serializer.is_valid(raise_exception=True)
    egresado = serializer.save()

    return egresado


def check_or_transform_data(data):
    ciudad_natal = get_or_create_ciudad(data=data.get("ciudad_natal"))

    ciudad_actual = get_or_create_ciudad(data=data.get("ciudad_actual"))

    egresado = {
        "dni": data.get("dni"),
        "nombres": data.get("nombres").title(),
        "apellidos": data.get("apellidos").title(),
        "email": data.get("email"),
        "fecha_nac": data.get("fecha_nac"),
        "nacionalidad": data.get("nacionalidad").title(),
        "ciudad_natal": ciudad_natal.id if ciudad_natal else None,
        "ciudad_actual": ciudad_actual.id if ciudad_actual else None,
        "sexo": data.get("sexo").title(),
    }

    return egresado


def egresado_exists(dni):
    return FwUser.objects.filter(dni=dni).exists()


def check_data_egresado(json_egresado):
    if not check_carrera_following(json_egresado.get("carrera")):
        return False

    if egresado_exists(dni=json_egresado.get("nro_documento")):
        return False

    return True


def set_origin(usuario, origen):
    usuario.origen = origen
    usuario.save()


def crear_nuevo_egresado(json_egresado):
    egresado = create_egresado(json_egresado=json_egresado)

    create_egreso(
        carrera_id=get_carrera_following(json_egresado.get("carrera")).id,
        usuario=egresado,
        ciclo_egreso=json_egresado.get("fecha_egreso"),
    )

    create_privacidad(usuario=egresado)

    set_origin(usuario=egresado, origen=2)

    return egresado


def check_and_set_origin(row):
    try:
        if not row["ORIGEN"]:
            row["ORIGEN"] = 1

    except Exception as e:
        print(e)


def get_egresado_by_dni(dni):
    return FwUser.objects.filter(dni=dni).first()


def filter_egresado_query(queryset, filters):
    filtered_queryset = queryset

    estado = filters.get("estado")

    dni = filters.get("dni")
    apellidos = filters.get("apellidos")
    nombres = filters.get("nombres")
    email = filters.get("email")
    nacionalidad = filters.get("nacionalidad")
    fecha_nac = filters.get("fecha_nac")
    sexo = filters.get("sexo")

    offset = filters.get("skip")
    limit = filters.get("limit")

    if estado:
        filtered_queryset = filtered_queryset.filter(is_active=estado)
    else:
        filtered_queryset = filtered_queryset.filter(is_active=True)

    if dni:
        filtered_queryset = filtered_queryset.filter(dni__icontains=dni)
    if apellidos:
        filtered_queryset = filtered_queryset.filter(apellidos__icontains=apellidos)
    if nombres:
        filtered_queryset = filtered_queryset.filter(nombres__icontains=nombres)
    if email:
        filtered_queryset = filtered_queryset.filter(email__icontains=email)
    if nacionalidad:
        filtered_queryset = filtered_queryset.filter(
            nacionalidad__icontains=nacionalidad
        )
    if fecha_nac:
        filtered_queryset = filtered_queryset.filter(fecha_nac__icontains=fecha_nac)
    if sexo:
        filtered_queryset = filtered_queryset.filter(sexo__icontains=sexo)

    if offset:
        filtered_queryset = filtered_queryset[int(offset) :]

    if limit:
        filtered_queryset = filtered_queryset[: int(limit)]

    return filtered_queryset
