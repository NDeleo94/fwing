from rest_framework import serializers

from apps.fw.models.puesto_model import Puesto


class PuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puesto
        fields = "__all__"


class PuestoReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Puesto
        exclude = ("estado",)


class PuestoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puesto
        fields = ("puesto",)
