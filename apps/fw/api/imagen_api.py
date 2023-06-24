from rest_framework import viewsets

from apps.fw.serializers.imagen_serializers import *


class ImagenAPIView(viewsets.ModelViewSet):
    serializer_class = ImagenSerializer
    queryset = serializer_class.Meta.model.objects.all()
