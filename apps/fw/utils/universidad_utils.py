from apps.fw.models.universidad_model import Universidad

from apps.fw.serializers.universidad_serializers import *


def create_universidad(data):
    data_cased = data.title()
    data_universidad = {
        "universidad": data_cased,
    }
    serializer = UniversidadUpdateSerializer(data=data_universidad)
    serializer.is_valid(raise_exception=True)
    universidad = serializer.save()

    return universidad


def get_universidad(data):
    if not data or type(data) is str:
        universidad = None
    else:
        universidad = Universidad.objects.get(id=data)

    return universidad


def get_or_create_universidad(data):
    universidad = get_universidad(data=data)

    if not universidad:
        universidad = create_universidad(data=data)

    return universidad
