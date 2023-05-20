from rest_framework import viewsets, mixins

from apps.fw.serializers.egresado_serializers import *


class EgresadoViewSet(
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
        if self.action == "update":
            return EgresadoUpdateSerializer
        return EgresadoReadOnlySerializer
