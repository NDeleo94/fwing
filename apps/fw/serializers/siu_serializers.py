from rest_framework import serializers
from apps.fw.models.log_siu_model import LogSIU


class LogSIUSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogSIU
        fields = "__all__"
