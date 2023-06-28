from rest_framework import viewsets, mixins

from apps.fw.serializers.actividad_serializers import *

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class ActividadUpdateAPIView(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = ActividadUpdateSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.save()
        return Response(
            {"message": "Actividad deleted"},
            status=status.HTTP_200_OK,
        )


class ActividadReadOnlyAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ActividadReadOnlySerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True).order_by(
        "inicio",
        "fin",
    )


class ActividadAPIView(viewsets.ModelViewSet):
    serializer_class = ActividadSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)
