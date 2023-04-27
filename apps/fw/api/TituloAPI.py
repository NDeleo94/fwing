from rest_framework import viewsets

from apps.fw.serializers.TituloSerializers import *


class TituloAPIView(viewsets.ModelViewSet):
    serializer_class = TituloSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)


class TituloListAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = TituloListSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)


class TituloDetailAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = TituloDetailSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)
