from rest_framework import serializers

from apps.fw.models.facultad_model import Facultad
from apps.fw.models.universidad_model import Universidad


class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultad
        fields = "__all__"


class UniversidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universidad
        fields = (
            "id",
            "universidad",
            "acronimo",
        )


class FacultadReadOnlySerializer(serializers.ModelSerializer):
    universidad = UniversidadSerializer()

    class Meta:
        model = Facultad
        fields = (
            "id",
            "facultad",
            "acronimo",
            "domicilio",
            "web",
            "email",
            "telefono",
            "universidad",
        )


class FacultadUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultad
        fields = (
            "facultad",
            "universidad",
        )
