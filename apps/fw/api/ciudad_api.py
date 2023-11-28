from rest_framework import viewsets, mixins

from apps.fw.serializers.ciudad_serializers import *

from apps.fw.utils.ciudad_utils import filter_ciudad_query

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class CiudadUpdateAPIView(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = CiudadReadOnlySerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.save()
        return Response(
            {"message": "Ciudad deleted"},
            status=status.HTTP_200_OK,
        )


class CiudadReadOnlyAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = CiudadReadOnlySerializer
    queryset = serializer_class.Meta.model.objects.all().order_by(
        "ciudad",
    )

    def get_queryset(self):
        queryset = super().get_queryset()

        filters = self.request.query_params

        return filter_ciudad_query(queryset=queryset, filters=filters)


class CiudadAPIView(viewsets.ModelViewSet):
    serializer_class = CiudadSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)
