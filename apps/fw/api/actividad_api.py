from rest_framework import viewsets

from apps.fw.serializers.actividad_serializers import *


class ActividadAPIView(viewsets.ModelViewSet):
    serializer_class = ActividadSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)


class ActividadListAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ActividadListSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)


class ActividadDetailAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ActividadDetailSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)
