from rest_framework import viewsets

from apps.fw.serializers.puesto_serializers import *


class PuestoAPIView(viewsets.ModelViewSet):
    serializer_class = PuestoSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)


class PuestoListAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = PuestoListSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)


class PuestoDetailAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = PuestoDetailSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)
