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
