from apps.fw.models import Organizacion

from apps.fw.serializers.organizacion_serializers import *


def get_or_create_organizacion(data):
    if type(data) is str:
        data_cased = data.title()
        data_organizacion = {
            "organizacion": data_cased,
        }
        serializer = OrganizacionUpdateSerializer(data=data_organizacion)
        serializer.is_valid(raise_exception=True)
        organizacion = serializer.save()
    else:
        organizacion = Organizacion.objects.get(id=data)

    return organizacion
