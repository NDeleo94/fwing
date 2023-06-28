from rest_framework import serializers

from apps.fw.models.universidad_model import Universidad


class UniversidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universidad
        fields = "__all__"


class UniversidadReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Universidad
        exclude = ("estado",)


class UniversidadUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universidad
        fields = (
            "id",
            "universidad",
        )
