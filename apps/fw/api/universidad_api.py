from rest_framework import viewsets, mixins

from apps.fw.serializers.universidad_serializers import *

from apps.fw.utils.universidad_utils import filter_universidad_query

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class UniversidadUpdateAPIView(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = UniversidadReadOnlySerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.save()
        return Response(
            {"message": "Universidad deleted"},
            status=status.HTTP_200_OK,
        )


class UniversidadReadOnlyAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = UniversidadReadOnlySerializer
    queryset = serializer_class.Meta.model.objects.all().order_by(
        "universidad",
    )

    def get_queryset(self):
        queryset = super().get_queryset()

        filters = self.request.query_params

        return filter_universidad_query(queryset=queryset, filters=filters)


class UniversidadAPIView(viewsets.ModelViewSet):
    serializer_class = UniversidadSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)
