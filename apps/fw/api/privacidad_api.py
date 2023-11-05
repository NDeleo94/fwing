from rest_framework import viewsets, mixins

from apps.fw.serializers.privacidad_serializers import *

from apps.fw.utils.privacidad_utils import check_privacity

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class PrivacidadUpdateAPIView(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = PrivacidadSerializer
    queryset = serializer_class.Meta.model.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def check_privacity(self, usuario):
        privacidad = Privacidad.objects.filter(
            usuario=usuario,
        ).first()
        if privacidad:
            return privacidad
        else:
            return False

    def create(self, request, *args, **kwargs):
        data = request.data

        privacidad = check_privacity(request.data.get("usuario"))

        if privacidad:
            serializer = self.get_serializer(privacidad, data=data)
        else:
            serializer = self.get_serializer(data=data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers,
        )


class PrivacidadReadOnlyAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = PrivacidadSerializer
    queryset = serializer_class.Meta.model.objects.all()


class PrivacidadAPIView(viewsets.ModelViewSet):
    serializer_class = PrivacidadSerializer
    queryset = serializer_class.Meta.model.objects.all()
