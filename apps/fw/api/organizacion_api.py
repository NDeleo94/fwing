from rest_framework import viewsets, mixins

from apps.fw.serializers.organizacion_serializers import *

from apps.fw.utils.organizacion_utils import filter_organizacion_query

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class OrganizacionUpdateAPIView(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = OrganizacionUpdateSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.save()
        return Response(
            {"message": "Organizacion deleted"},
            status=status.HTTP_200_OK,
        )


class OrganizacionReadOnlyAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrganizacionReadOnlySerializer
    queryset = serializer_class.Meta.model.objects.all().order_by(
        "organizacion",
    )

    def get_queryset(self):
        queryset = super().get_queryset()

        filters = self.request.query_params

        return filter_organizacion_query(queryset=queryset, filters=filters)


class OrganizacionAPIView(viewsets.ModelViewSet):
    serializer_class = OrganizacionSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)
