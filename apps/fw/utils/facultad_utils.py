from apps.fw.models.facultad_model import Facultad

from apps.fw.serializers.facultad_serializers import *


def create_facultad(data, universidad_id):
    data_cased = data.title()
    data_facultad = {
        "facultad": data_cased,
        "universidad": universidad_id,
    }
    serializer = FacultadUpdateSerializer(data=data_facultad)
    serializer.is_valid(raise_exception=True)
    facultad = serializer.save()

    return facultad


def get_facultad(data):
    if not data or type(data) is str:
        facultad = None
    else:
        facultad = Facultad.objects.get(id=data)

    return facultad


def get_or_create_facultad(data, universidad_id):
    facultad = get_facultad(data=data)

    if not facultad:
        facultad = create_facultad(
            data=data,
            universidad_id=universidad_id,
        )

    return facultad


def filter_facultad_query(queryset, filters):
    filtered_queryset = queryset

    estado = filters.get("estado")

    facultad = filters.get("facultad")
    acronimo = filters.get("acronimo")

    offset = filters.get("skip")
    limit = filters.get("limit")

    if estado:
        filtered_queryset = filtered_queryset.filter(estado=estado)
    else:
        filtered_queryset = filtered_queryset.filter(estado=True)

    if facultad:
        filtered_queryset = filtered_queryset.filter(facultad__icontains=facultad)
    if acronimo:
        filtered_queryset = filtered_queryset.filter(acronimo__icontains=acronimo)

    if offset:
        filtered_queryset = filtered_queryset[int(offset) :]

    if limit:
        filtered_queryset = filtered_queryset[: int(limit)]

    return filtered_queryset
