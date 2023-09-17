from apps.fw.models.ciudad_model import Ciudad

from apps.fw.serializers.ciudad_serializers import *


def get_or_create_ciudad(data):
    if not data:
        ciudad = None
    elif type(data) is str:
        data_cased = data.title()
        data_ciudad = {
            "ciudad": data_cased,
        }
        serializer = CiudadUpdateSerializer(data=data_ciudad)
        serializer.is_valid(raise_exception=True)
        ciudad = serializer.save()
    else:
        ciudad = Ciudad.objects.get(id=data)

    return ciudad
