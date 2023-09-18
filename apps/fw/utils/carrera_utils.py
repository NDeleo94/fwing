from apps.fw.models.carrera_model import Carrera

from apps.fw.serializers.carrera_serializers import *


def get_or_create_carrera(data, facultad):
    if type(data) is str:
        data_cased = data.title()
        data_carrera = {
            "carrera": data_cased,
            "facultad": facultad,
        }
        serializer = CarreraUpdateSerializer(data=data_carrera)
        serializer.is_valid(raise_exception=True)
        carrera = serializer.save()
    else:
        carrera = Carrera.objects.get(id=data)

    return carrera
