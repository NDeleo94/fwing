from rest_framework import serializers

from apps.fw.models.email_model import Email


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = "__all__"


class EmailReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        exclude = ("estado",)


class EmailUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = (
            "plantilla",
            "asunto",
            "cuerpo",
        )
