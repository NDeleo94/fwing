from rest_framework import viewsets

from apps.fw.serializers.egreso_serializers import *


class EgresoAPIView(viewsets.ModelViewSet):
    serializer_class = EgresoSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)


class EgresoListAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = EgresoListSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)


class EgresoDetailAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = EgresoDetailSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)
