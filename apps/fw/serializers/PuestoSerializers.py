from rest_framework import serializers

from apps.fw.models.puesto import Puesto


class PuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puesto
        fields = "__all__"


class PuestoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puesto
        fields = (
            "id",
            "puesto",
        )


class PuestoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puesto
        exclude = ("estado",)
