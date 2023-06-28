from rest_framework import viewsets, mixins

from apps.fw.serializers.actividad_serializers import *
from apps.fw.serializers.organizacion_serializers import *
from apps.fw.serializers.puesto_serializers import *

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class ActividadUpdateAPIView(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = ActividadUpdateSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_or_create_organizacion(self, data):
        if type(data) is str:
            data_organizacion = {
                "organizacion": data,
            }
            serializer = OrganizacionUpdateSerializer(data=data_organizacion)
            serializer.is_valid(raise_exception=True)
            organizacion = serializer.save()
        else:
            organizacion = Organizacion.objects.get(id=data)

        return organizacion

    def get_or_create_puesto(self, data):
        if type(data) is str:
            data_puesto = {
                "puesto": data,
            }
            serializer = PuestoUpdateSerializer(data=data_puesto)
            serializer.is_valid(raise_exception=True)
            puesto = serializer.save()
        else:
            puesto = Puesto.objects.get(id=data)

        return puesto

    def check_or_transform_data(self, data):
        # Checkear organizacion
        organizacion = self.get_or_create_organizacion(data=data["organizacion"])
        # Checkear puesto
        puesto = self.get_or_create_puesto(data=data["puesto"])

        # Devolver actividad completo
        data_transformed = {
            "inicio": data["inicio"],
            "fin": data["fin"],
            "usuario": data["usuario"],
            "organizacion": organizacion.id,
            "puesto": puesto.id,
        }
        return data_transformed

    def create(self, request, *args, **kwargs):
        # Checkear actividad
        data = self.check_or_transform_data(request.data)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers,
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.save()
        return Response(
            {"message": "Actividad deleted"},
            status=status.HTTP_200_OK,
        )


class ActividadReadOnlyAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ActividadReadOnlySerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True).order_by(
        "inicio",
        "fin",
    )


class ActividadAPIView(viewsets.ModelViewSet):
    serializer_class = ActividadSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)
