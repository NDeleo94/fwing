from rest_framework import serializers


class NewPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)
