from rest_framework import serializers

from apps.fw.models.imagen_model import Imagen


class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = "__all__"
