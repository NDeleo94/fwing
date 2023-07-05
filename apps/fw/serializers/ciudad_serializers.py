from rest_framework import serializers

from apps.fw.models.ciudad_model import Ciudad


class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = "__all__"


class CiudadReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        exclude = ("estado",)


class CiudadUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = (
            "id",
            "ciudad",
        )
