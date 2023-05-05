from rest_framework import viewsets

from apps.fw.serializers.universidad_serializers import *


class UniversidadAPIView(viewsets.ModelViewSet):
    serializer_class = UniversidadSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)


class UniversidadListAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = UniversidadListSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)


class UniversidadDetailAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = UniversidadDetailSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)
