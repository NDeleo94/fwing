from rest_framework import serializers

from apps.fw.models.organizacion import Organizacion


class OrganizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizacion
        fields = "__all__"


class OrganizacionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizacion
        fields = (
            "id",
            "organizacion",
        )


class OrganizacionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizacion
        exclude = ("estado",)
