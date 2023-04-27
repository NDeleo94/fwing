from rest_framework import serializers

from apps.fw.models.carrera import Titulo


class TituloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Titulo
        fields = "__all__"


class TituloListSerializer(serializers.ModelSerializer):
    carrera = serializers.StringRelatedField()

    class Meta:
        model = Titulo
        fields = (
            "id",
            "titulo",
            "carrera",
        )


class TituloDetailSerializer(serializers.ModelSerializer):
    carrera = serializers.StringRelatedField()

    class Meta:
        model = Titulo
        exclude = ("estado",)
