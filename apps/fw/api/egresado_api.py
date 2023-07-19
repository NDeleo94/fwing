from rest_framework import viewsets, mixins

from apps.fw.serializers.egresado_serializers import *
from apps.fw.serializers.egreso_serializers import *
from apps.fw.serializers.ciudad_serializers import *

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class EgresadoUpdateAPIView(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = FwUser.objects.all()
    serializer_class = EgresadoUpdateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_or_create_ciudad(self, data):
        if not data:
            ciudad = None
        elif type(data) is str:
            data_cased = data.title()
            data_ciudad = {
                "ciudad": data_cased,
            }
            serializer = CiudadUpdateSerializer(data=data_ciudad)
            serializer.is_valid(raise_exception=True)
            ciudad = serializer.save()
        else:
            ciudad = Ciudad.objects.get(id=data)

        return ciudad

    def create_egreso(self, egresado, data):
        data_egreso = {
            "usuario": egresado.id,
            "carrera": data["carrera"],
            "ciclo_egreso": data["ciclo_egreso"],
        }
        serializer = EgresadoUpdateSerializer(data=data_egreso)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def create_privacidad(self, egresado):
        data_privacidad = {
            "usuario": egresado.id,
        }
        serializer = PrivacidadSerializer(data=data_privacidad)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def set_origin(self, egresado):
        egresado.origin = 3
        egresado.save()

    def check_or_transform_data(self, data):
        ciudad_natal = self.get_or_create_ciudad(data=data["ciudad_natal"])

        ciudad_actual = self.get_or_create_ciudad(data=data["ciudad_actual"])

        egresado = {
            "dni": data["dni"],
            "nombres": data["nombres"],
            "apellidos": data["apellidos"],
            "email": data["email"],
            "fecha_nac": data["fecha_nac"],
            "nacionalidad": data["nacionalidad"],
            "ciudad_natal": ciudad_natal.id,
            "ciudad_actual": ciudad_actual.id,
            "sexo": data["sexo"],
        }

        return egresado

    def create(self, request, *args, **kwargs):
        data_egresado = self.check_or_transform_data(request.data)
        serializer = self.get_serializer(data=data_egresado)
        serializer.is_valid(raise_exception=True)
        egresado = serializer.save()

        self.create_egreso(egresado=egresado, data=request.data)

        self.create_privacidad(egresado=egresado)

        self.set_origin(egresado=egresado)

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers,
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(
            {"message": "Egresado deleted"},
            status=status.HTTP_200_OK,
        )


class EgresadoReadOnlyAPIView(
    viewsets.ReadOnlyModelViewSet,
):
    queryset = FwUser.objects.filter(is_active=True).order_by(
        "apellidos",
        "nombres",
    )
    serializer_class = EgresadoReadOnlySerializer


class EgresadoViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """
    A viewset that provides `retrieve`, `update`, and `list` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """

    pass


class EgresadoAPIView(EgresadoViewSet):
    queryset = FwUser.objects.filter(is_active=True)

    def get_serializer_class(self):
        if self.action in ["create", "update"]:
            return EgresadoUpdateSerializer
        return EgresadoReadOnlySerializer
