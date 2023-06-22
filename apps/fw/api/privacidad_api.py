from rest_framework import viewsets

from apps.fw.serializers.privacidad_serializers import *


class PrivacidadAPIView(viewsets.ModelViewSet):
    serializer_class = PrivacidadSerializer
    queryset = serializer_class.Meta.model.objects.all()
