from apps.fw.serializers.egreso_serializers import EgresoUpdateSerializer

from apps.fw.utils.universidad_utils import get_or_create_universidad
from apps.fw.utils.facultad_utils import get_or_create_facultad
from apps.fw.utils.carrera_utils import get_or_create_carrera


def check_or_transform_data(data):
    universidad = get_or_create_universidad(
        data=data.get("universidad"),
    )
    facultad = get_or_create_facultad(
        data=data.get("facultad"),
        universidad_id=universidad.id,
    )
    carrera = get_or_create_carrera(
        data=data.get("carrera"),
        facultad_id=facultad.id,
    )

    data_transformed = {
        "universidad": universidad.id,
        "facultad": facultad.id,
        "carrera": carrera.id,
        "usuario": data.get("usuario"),
        "ciclo_egreso": data.get("ciclo_egreso"),
        "matricula": data.get("matricula"),
        "postgrado": data.get("postgrado"),
    }

    return data_transformed


def create_egreso(carrera_id, usuario, ciclo_egreso):
    data_egreso = {
        "carrera": carrera_id,
        "usuario": usuario.id,
        "ciclo_egreso": ciclo_egreso,
    }
    serializer = EgresoUpdateSerializer(data=data_egreso)
    serializer.is_valid(raise_exception=True)
    egreso = serializer.save()
    return egreso


def filter_egreso_query(queryset, filters):
    filtered_queryset = queryset

    estado = filters.get("estado")

    ciclo_egreso = filters.get("ciclo_egreso")
    matricula = filters.get("matricula")

    offset = filters.get("skip")
    limit = filters.get("limit")

    if estado:
        filtered_queryset = filtered_queryset.filter(estado=estado)
    else:
        filtered_queryset = filtered_queryset.filter(estado=True)

    if ciclo_egreso:
        filtered_queryset = filtered_queryset.filter(
            ciclo_egreso__icontains=ciclo_egreso
        )
    if matricula:
        filtered_queryset = filtered_queryset.filter(matricula__icontains=matricula)

    if offset:
        filtered_queryset = filtered_queryset[int(offset) :]

    if limit:
        filtered_queryset = filtered_queryset[: int(limit)]

    return filtered_queryset
