from rest_framework import viewsets, mixins

from apps.fw.serializers.organizacion_serializers import *

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
    queryset = serializer_class.Meta.model.objects.filter(estado=True).order_by(
        "organizacion",
    )


class OrganizacionAPIView(viewsets.ModelViewSet):
    serializer_class = OrganizacionSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)
