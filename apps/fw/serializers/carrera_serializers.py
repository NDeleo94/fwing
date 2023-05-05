from rest_framework import serializers

from apps.fw.models.carrera_model import Carrera


class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = "__all__"


class CarreraListSerializer(serializers.ModelSerializer):
    facultad = serializers.StringRelatedField()

    class Meta:
        model = Carrera
        fields = (
            "id",
            "carrera",
            "facultad",
        )


class CarreraDetailSerializer(serializers.ModelSerializer):
    facultad = serializers.StringRelatedField()

    class Meta:
        model = Carrera
        exclude = ("estado",)
