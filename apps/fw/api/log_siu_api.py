from rest_framework import viewsets

from apps.fw.serializers.siu_serializers import *

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class LogSIUAPIView(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = LogSIUSerializer
    queryset = serializer_class.Meta.model.objects.all().order_by(
        "fecha",
    )
