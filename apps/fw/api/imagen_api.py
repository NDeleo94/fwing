from rest_framework import viewsets, mixins

from apps.fw.serializers.imagen_serializers import *

from apps.fw.utils.imagen_utils import (
    check_profile_picture,
    check_or_transform_data,
)

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class ImagenUpdateAPIView(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = ImagenSerializer
    queryset = serializer_class.Meta.model.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Checkear imagen
        data = check_or_transform_data(request.data)
        # Checkear foto de perfil
        imagen = check_profile_picture(request.data["usuario"])

        if imagen:
            serializer = self.get_serializer(imagen, data=data)
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

    def destroy(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        instance = self.check_profile_picture(pk)
        if instance:
            instance.estado = False
            instance.file = None
            instance.url = None
            instance.save()
            return Response(
                {"message": "Imagen deleted"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"message": "Imagen No Found"},
            status=status.HTTP_404_NOT_FOUND,
        )


class ImagenReadOnlyAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ImagenSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)


class ImagenAPIView(viewsets.ModelViewSet):
    serializer_class = ImagenSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)
