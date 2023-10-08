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
    fecha_nac_egresado = title_case(json_egresado, "fecha_nacimiento")
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
        carrera=get_carrera_following(json_egresado.get("carrera")),
        usuario=egresado,
        json_egresado=json_egresado,
    )

    create_privacidad(usuario=egresado)

    set_origin(usuario=egresado, origen=2)

    return egresado
