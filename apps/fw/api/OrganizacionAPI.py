from rest_framework import viewsets

from apps.fw.serializers.OrganizacionSerializers import *


class OrganizacionAPIView(viewsets.ModelViewSet):
    serializer_class = OrganizacionSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)


class OrganizacionListAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrganizacionListSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)


class OrganizacionDetailAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrganizacionDetailSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)
