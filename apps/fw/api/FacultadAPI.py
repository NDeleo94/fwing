from rest_framework import viewsets

from apps.fw.serializers.FacultadSerializers import *


class FacultadAPIView(viewsets.ModelViewSet):
    serializer_class = FacultadSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)


class FacultadListAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = FacultadListSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)


class FacultadDetailAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = FacultadDetailSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)
