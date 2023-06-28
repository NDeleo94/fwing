from rest_framework import viewsets, mixins

from apps.fw.serializers.facultad_serializers import *

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class FacultadUpdateAPIView(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = FacultadUpdateSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.save()
        return Response(
            {"message": "Facultad deleted"},
            status=status.HTTP_200_OK,
        )


class FacultadReadOnlyAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = FacultadReadOnlySerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True).order_by(
        "facultad",
        "universidad",
    )


class FacultadAPIView(viewsets.ModelViewSet):
    serializer_class = FacultadSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)
