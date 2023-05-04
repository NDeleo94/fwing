from rest_framework import serializers

from apps.fw.models.egreso import Egreso


class EgresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Egreso
        fields = "__all__"


class EgresoListSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField()
    carrera = serializers.StringRelatedField()

    class Meta:
        model = Egreso
        fields = (
            "id",
            "ciclo_egreso",
            "matricula",
            "usuario",
            "carrera",
        )


class EgresoDetailSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField()
    carrera = serializers.StringRelatedField()

    class Meta:
        model = Egreso
        fields = (
            "id",
            "ciclo_egreso",
            "matricula",
            "usuario",
            "carrera",
        )
