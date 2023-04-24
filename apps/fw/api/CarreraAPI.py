from rest_framework import viewsets

from apps.fw.serializers.CarreraSerializers import *


class CarreraAPIView(viewsets.ModelViewSet):
    serializer_class = CarreraSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)


class CarreraListAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = CarreraListSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)


class CarreraDetailAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = CarreraDetailSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)
