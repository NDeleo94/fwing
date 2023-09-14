from rest_framework import viewsets

from apps.fw.serializers.mapamundi_serializers import *


class ActividadMapaMundiAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ActividadMapaMundiSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True).order_by(
        "inicio",
        "fin",
    )
