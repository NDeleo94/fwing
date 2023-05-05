from rest_framework import serializers

from apps.fw.models.actividad_model import Actividad


class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = "__all__"


class ActividadListSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField()
    organizacion = serializers.StringRelatedField()
    puesto = serializers.StringRelatedField()

    class Meta:
        model = Actividad
        exclude = ("estado",)


class ActividadDetailSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField()
    organizacion = serializers.StringRelatedField()
    puesto = serializers.StringRelatedField()

    class Meta:
        model = Actividad
        exclude = ("estado",)
