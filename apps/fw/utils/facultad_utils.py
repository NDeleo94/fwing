from apps.fw.models.facultad_model import Facultad

from apps.fw.serializers.facultad_serializers import *


def get_or_create_facultad(data, universidad):
    if type(data) is str:
        data_cased = data.title()
        data_facultad = {
            "facultad": data_cased,
            "universidad": universidad,
        }
        serializer = FacultadUpdateSerializer(data=data_facultad)
        serializer.is_valid(raise_exception=True)
        facultad = serializer.save()
    else:
        facultad = Facultad.objects.get(id=data)

    return facultad
