from rest_framework import viewsets

from apps.fw.serializers.egresado_serializers import *


class EgresadoAPIView(viewsets.ModelViewSet):
    serializer_class = EgresadoSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)


class EgresadoListAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = EgresadoListSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)


class EgresadoDetailAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = EgresadoDetailSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)
