from rest_framework import serializers

from apps.fw.models.egreso_model import Egreso
from apps.fw.models.universidad_model import Universidad
from apps.fw.models.facultad_model import Facultad
from apps.fw.models.carrera_model import Carrera
from apps.fw.models.user_model import FwUser


class EgresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Egreso
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


class CarreraSerializer(serializers.ModelSerializer):
    facultad = FacultadSerializer()

    class Meta:
        model = Carrera
        fields = (
            "id",
            "carrera",
            "facultad",
        )


class EgresadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FwUser
        fields = (
            "id",
            "apellidos",
            "nombres",
        )


class EgresoReadOnlySerializer(serializers.ModelSerializer):
    usuario = EgresadoSerializer()
    carrera = CarreraSerializer()

    class Meta:
        model = Egreso
        fields = (
            "id",
            "ciclo_egreso",
            "matricula",
            "usuario",
            "carrera",
        )


class EgresoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Egreso
        fields = (
            "id",
            "matricula",
            "ciclo_egreso",
            "usuario",
            "carrera",
        )
