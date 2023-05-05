from rest_framework import serializers

from apps.fw.models.facultad_model import Facultad


class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultad
        fields = "__all__"


class FacultadListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultad
        fields = (
            "id",
            "facultad",
            "acronimo",
        )


class FacultadDetailSerializer(serializers.ModelSerializer):
    universidad = serializers.StringRelatedField()

    class Meta:
        model = Facultad
        exclude = ("estado",)
