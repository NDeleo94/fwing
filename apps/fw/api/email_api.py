from rest_framework import viewsets, mixins

from apps.fw.serializers.email_serializers import *

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class EmailUpdateAPIView(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = EmailUpdateSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.save()
        return Response(
            {"message": "Email deleted"},
            status=status.HTTP_200_OK,
        )


class EmailReadOnlyAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = EmailReadOnlySerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True).order_by(
        "plantilla",
    )


class EmailAPIView(viewsets.ModelViewSet):
    serializer_class = EmailSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)
