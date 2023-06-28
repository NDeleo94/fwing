from rest_framework import serializers

from apps.fw.models.carrera_model import Carrera
from apps.fw.models.facultad_model import Facultad
from apps.fw.models.universidad_model import Universidad


class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = "__all__"


class UniversidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universidad
        fields = (
            "id",
            "universidad",
            "acronimo",
        )


class FacultadSerializer(serializers.ModelSerializer):
    universidad = UniversidadSerializer()

    class Meta:
        model = Facultad
        fields = (
            "id",
            "facultad",
            "acronimo",
            "universidad",
        )


class CarreraReadOnlySerializer(serializers.ModelSerializer):
    facultad = FacultadSerializer()

    class Meta:
        model = Carrera
        fields = (
            "id",
            "carrera",
            "web",
            "following",
            "facultad",
        )


class CarreraUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = (
            "id",
            "carrera",
            "following",
            "facultad",
        )
