from rest_framework import serializers

from apps.fw.models.universidad import Universidad


class UniversidadListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universidad
        fields = (
            "id",
            "universidad",
            "acronimo",
        )


class UniversidadDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universidad
        exclude = ("estado",)
