from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination

from apps.fw.serializers.egresado_serializers import *


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


class EgresadosPagination(PageNumberPagination):
    page_size = 50


class EgresadoAPIView(EgresadoViewSet):
    queryset = FwUser.objects.filter(is_active=True).order_by(
        "apellidos",
        "nombres",
    )
    pagination_class = EgresadosPagination

    def get_serializer_class(self):
        if self.action in ["create", "update"]:
            return EgresadoUpdateSerializer
        return EgresadoReadOnlySerializer
