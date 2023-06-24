from rest_framework import viewsets, mixins

from apps.fw.serializers.egresado_serializers import *

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class EgresadoUpdateAPIView(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = FwUser.objects.all()
    serializer_class = EgresadoUpdateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class EgresadoReadOnlyAPIView(
    viewsets.ReadOnlyModelViewSet,
):
    queryset = FwUser.objects.filter(is_active=True).order_by(
        "apellidos",
        "nombres",
    )
    serializer_class = EgresadoReadOnlySerializer


class EgresadoViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """
    A viewset that provides `retrieve`, `update`, and `list` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """

    pass


class EgresadoAPIView(EgresadoViewSet):
    queryset = FwUser.objects.filter(is_active=True)

    def get_serializer_class(self):
        if self.action in ["create", "update"]:
            return EgresadoUpdateSerializer
        return EgresadoReadOnlySerializer
