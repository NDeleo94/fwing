from rest_framework import serializers

from apps.fw.models.organizacion_model import Organizacion


class OrganizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizacion
        fields = "__all__"


class OrganizacionReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizacion
        exclude = ("estado",)


class OrganizacionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizacion
        fields = ("organizacion",)
