from rest_framework import viewsets

from apps.fw.serializers.egresado_serializers import *


class EgresadoReadOnlyAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = EgresadoReadOnlySerializer
    queryset = serializer_class.Meta.model.objects.filter(is_active=True)
