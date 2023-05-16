from rest_framework import serializers

from apps.fw.models.user_model import FwUser


class EgresadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FwUser
        fields = (
            "id",
            "email",
            "apellidos",
            "nombres",
            "nacionalidad",
            "fecha_nac",
            "ciudad_natal",
            "ciudad_actual",
            "last_login",
        )


class EgresadoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FwUser
        fields = (
            "id",
            "email",
            "apellidos",
            "nombres",
            "nacionalidad",
            "fecha_nac",
            "ciudad_natal",
            "ciudad_actual",
        )


class EgresadoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FwUser
        fields = (
            "id",
            "email",
            "apellidos",
            "nombres",
            "nacionalidad",
            "fecha_nac",
            "ciudad_natal",
            "ciudad_actual",
        )
