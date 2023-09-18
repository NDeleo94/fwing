from apps.fw.models.universidad_model import Universidad

from apps.fw.serializers.universidad_serializers import *


def get_or_create_universidad(data):
    if type(data) is str:
        data_cased = data.title()
        data_universidad = {
            "universidad": data_cased,
        }
        serializer = UniversidadUpdateSerializer(data=data_universidad)
        serializer.is_valid(raise_exception=True)
        universidad = serializer.save()
    else:
        universidad = Universidad.objects.get(id=data)

    return universidad
