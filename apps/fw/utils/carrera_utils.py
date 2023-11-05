from apps.fw.models.carrera_model import Carrera

from apps.fw.serializers.carrera_serializers import *


def check_carrera_following(carrera):
    carrera = Carrera.objects.filter(
        carrera__icontains=carrera,
        following=True,
    ).first()

    if carrera:
        return True

    return False


def get_carrera_following(carrera):
    return Carrera.objects.filter(
        carrera__icontains=carrera,
        following=True,
    ).first()


def create_carrera(data, facultad_id):
    data_cased = data.title()
    data_carrera = {
        "carrera": data_cased,
        "facultad": facultad_id,
    }
    serializer = CarreraUpdateSerializer(data=data_carrera)
    serializer.is_valid(raise_exception=True)
    carrera = serializer.save()

    return carrera


def get_carrera(data):
    if not data or type(data) is str:
        carrera = None
    else:
        carrera = Carrera.objects.get(id=data)

    return carrera


def get_or_create_carrera(data, facultad_id):
    carrera = get_carrera(data=data)

    if not carrera:
        carrera = create_carrera(
            data=data,
            facultad_id=facultad_id,
        )

    return carrera


def filter_carrera_query(queryset, filters):
    filtered_queryset = queryset

    estado = filters.get("estado")

    carrera = filters.get("carrera")

    offset = filters.get("skip")
    limit = filters.get("limit")

    if estado:
        filtered_queryset = filtered_queryset.filter(estado=estado)
    else:
        filtered_queryset = filtered_queryset.filter(estado=True)

    if carrera:
        filtered_queryset = filtered_queryset.filter(carrera__icontains=carrera)

    if offset:
        filtered_queryset = filtered_queryset[int(offset) :]

    if limit:
        filtered_queryset = filtered_queryset[: int(limit)]

    return filtered_queryset
