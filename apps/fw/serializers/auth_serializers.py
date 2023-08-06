from rest_framework import serializers


class NewPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class ChangeEmailSerializer(serializers.Serializer):
    old_email = serializers.EmailField(required=True)
    new_email = serializers.EmailField(required=True)
