from rest_framework import viewsets, mixins

from apps.fw.serializers.universidad_serializers import *

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class UniversidadUpdateAPIView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = UniversidadReadOnlySerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class UniversidadReadOnlyAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = UniversidadReadOnlySerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)


class UniversidadAPIView(viewsets.ModelViewSet):
    serializer_class = UniversidadSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)
