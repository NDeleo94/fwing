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


def filter_puesto_query(queryset, filters):
    filtered_queryset = queryset

    estado = filters.get("estado")

    puesto = filters.get("puesto")
    descripcion = filters.get("descripcion")

    offset = filters.get("skip")
    limit = filters.get("limit")

    if estado:
        filtered_queryset = filtered_queryset.filter(estado=estado)
    else:
        filtered_queryset = filtered_queryset.filter(estado=True)

    if puesto:
        filtered_queryset = filtered_queryset.filter(puesto__icontains=puesto)
    if descripcion:
        filtered_queryset = filtered_queryset.filter(descripcion__icontains=descripcion)

    if offset:
        filtered_queryset = filtered_queryset[int(offset) :]

    if limit:
        filtered_queryset = filtered_queryset[: int(limit)]

    return filtered_queryset
