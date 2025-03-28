from rest_framework import viewsets, mixins

from apps.fw.serializers.puesto_serializers import *

from apps.fw.utils.puesto_utils import filter_puesto_query

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class PuestoUpdateAPIView(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = PuestoUpdateSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.save()
        return Response(
            {"message": "Puesto deleted"},
            status=status.HTTP_200_OK,
        )


class PuestoReadOnlyAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = PuestoReadOnlySerializer
    queryset = serializer_class.Meta.model.objects.all().order_by(
        "puesto",
    )

    def get_queryset(self):
        queryset = super().get_queryset()

        filters = self.request.query_params

        return filter_puesto_query(queryset=queryset, filters=filters)


class PuestoAPIView(viewsets.ModelViewSet):
    serializer_class = PuestoSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)
