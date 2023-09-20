from rest_framework import viewsets

from apps.fw.serializers.siu_serializers import *


class LogSIUAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = LogSIUSerializer
    queryset = serializer_class.Meta.model.objects.all().order_by(
        "fecha",
    )
