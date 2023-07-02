from rest_framework import viewsets, mixins

from apps.fw.serializers.imagen_serializers import *

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from google.auth import jwt


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

    def check_profile_picture(self, usuario):
        imagen = Imagen.objects.filter(
            usuario=usuario,
            perfil=True,
        ).first()
        if imagen:
            return imagen
        else:
            return False

    def get_google_property(self, token, property):
        try:
            decoded_token = jwt.decode(token, verify=False)
            google_email = decoded_token.get(property)
            return google_email
        except jwt.exceptions.DecodeError as e:
            print(f"Error decoding Google token: {e}")
            return None

    def check_or_transform_data(self, data):
        # Si es imagen subida
        if data["file"]:
            file = data["file"]
            url = None
        # Si es imagen de google
        else:
            file = None
            url = self.get_google_property(data["url"], "picture")

        # Devolver actividad completo
        data_transformed = {
            "usuario": data["usuario"],
            "file": file,
            "url": url,
            "perfil": True,
            "estado": True,
        }
        return data_transformed

    def create(self, request, *args, **kwargs):
        # Checkear imagen
        data = self.check_or_transform_data(request.data)
        # Checkear foto de perfil
        imagen = self.check_profile_picture(request.data["usuario"])

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
