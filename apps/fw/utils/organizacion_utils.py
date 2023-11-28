from apps.fw.models.organizacion_model import Organizacion

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


def filter_organizacion_query(queryset, filters):
    filtered_queryset = queryset

    estado = filters.get("estado")

    organizacion = filters.get("organizacion")
    tipo = filters.get("tipo")
    empleados = filters.get("empleados")
    descripcion = filters.get("descripcion")

    offset = filters.get("skip")
    limit = filters.get("limit")

    if estado:
        filtered_queryset = filtered_queryset.filter(estado=estado)
    else:
        filtered_queryset = filtered_queryset.filter(estado=True)

    if organizacion:
        filtered_queryset = filtered_queryset.filter(
            organizacion__icontains=organizacion
        )
    if tipo:
        filtered_queryset = filtered_queryset.filter(tipo__icontains=tipo)
    if empleados:
        filtered_queryset = filtered_queryset.filter(empleados=empleados)
    if descripcion:
        filtered_queryset = filtered_queryset.filter(descripcion__icontains=descripcion)

    if offset:
        filtered_queryset = filtered_queryset[int(offset) :]

    if limit:
        filtered_queryset = filtered_queryset[: int(limit)]

    return filtered_queryset
