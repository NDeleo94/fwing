from rest_framework import viewsets

from apps.fw.serializers.UniversidadSerializers import *


class UniversidadListAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = UniversidadListSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)


class UniversidadDetailAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = UniversidadDetailSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)
