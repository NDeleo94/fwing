from rest_framework import serializers

from apps.fw.models.actividad_model import Actividad
from apps.fw.models.user_model import FwUser
from apps.fw.models.organizacion_model import Organizacion
from apps.fw.models.puesto_model import Puesto
from apps.fw.models.ciudad_model import Ciudad


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


class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = (
            "id",
            "ciudad",
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
    ciudad = CiudadSerializer()

    class Meta:
        model = Actividad
        exclude = ("estado",)


class ActividadUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = (
            "id",
            "inicio",
            "fin",
            "usuario",
            "organizacion",
            "puesto",
            "ciudad",
            "modalidad",
            "seniority",
        )
