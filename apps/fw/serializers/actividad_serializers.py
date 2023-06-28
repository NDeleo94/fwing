from rest_framework import serializers

from apps.fw.models.actividad_model import Actividad
from apps.fw.models.user_model import FwUser
from apps.fw.models.organizacion_model import Organizacion
from apps.fw.models.puesto_model import Puesto


class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = "__all__"


class PuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puesto
        fields = (
            "id",
            "puesto",
        )


class OrganizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizacion
        fields = (
            "id",
            "organizacion",
        )


class EgresadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FwUser
        fields = (
            "id",
            "apellidos",
            "nombres",
        )


class EgresadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FwUser
        fields = (
            "id",
            "apellidos",
            "nombres",
        )


class ActividadReadOnlySerializer(serializers.ModelSerializer):
    usuario = EgresadoSerializer()
    organizacion = OrganizacionSerializer()
    puesto = PuestoSerializer()

    class Meta:
        model = Actividad
        exclude = ("estado",)


class ActividadUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = (
            "inicio",
            "fin",
            "usuario",
            "organizacion",
            "puesto",
        )
