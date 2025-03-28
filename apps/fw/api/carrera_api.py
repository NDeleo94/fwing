from rest_framework import viewsets, mixins

from apps.fw.serializers.carrera_serializers import *

from apps.fw.utils.carrera_utils import filter_carrera_query

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class CarreraUpdateAPIView(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = CarreraUpdateSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.save()
        return Response(
            {"message": "Carrera deleted"},
            status=status.HTTP_200_OK,
        )


class CarreraReadOnlyAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = CarreraReadOnlySerializer
    queryset = serializer_class.Meta.model.objects.all().order_by(
        "carrera",
        "facultad",
    )

    def get_queryset(self):
        queryset = super().get_queryset()

        filters = self.request.query_params

        return filter_carrera_query(queryset=queryset, filters=filters)


class CarreraAPIView(viewsets.ModelViewSet):
    serializer_class = CarreraSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)
