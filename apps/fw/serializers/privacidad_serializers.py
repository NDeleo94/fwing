from rest_framework import serializers

from apps.fw.models.privacidad_model import Privacidad


class PrivacidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Privacidad
        fields = "__all__"
