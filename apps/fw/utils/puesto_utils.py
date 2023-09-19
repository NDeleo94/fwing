from apps.fw.models.puesto_model import Puesto

from apps.fw.serializers.puesto_serializers import *


def get_or_create_puesto(data):
    if type(data) is str:
        data_cased = data.title()
        data_puesto = {
            "puesto": data_cased,
        }
        serializer = PuestoUpdateSerializer(data=data_puesto)
        serializer.is_valid(raise_exception=True)
        puesto = serializer.save()
    else:
        puesto = Puesto.objects.get(id=data)

    return puesto
