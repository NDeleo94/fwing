from rest_framework import viewsets, mixins

from apps.fw.serializers.egresado_serializers import *
from apps.fw.serializers.egreso_serializers import *
from apps.fw.serializers.ciudad_serializers import *

from apps.fw.utils.ciudad_utils import get_or_create_ciudad

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

    def create_egreso(self, egresado, data):
        data_egreso = {
            "usuario": egresado.id,
            "carrera": data["carrera"],
            "ciclo_egreso": data["ciclo_egreso"],
        }
        serializer = EgresoUpdateSerializer(data=data_egreso)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def create_privacidad(self, egresado):
        Privacidad.objects.create(usuario=egresado)
        # data_privacidad = {
        #     "usuario": egresado.id,
        # }
        # serializer = PrivacidadSerializer(data=data_privacidad)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()

    def set_origin(self, egresado):
        egresado.origen = 3
        egresado.save()

    def check_or_transform_data(self, data):
        ciudad_natal = get_or_create_ciudad(data=data["ciudad_natal"])

        ciudad_actual = get_or_create_ciudad(data=data["ciudad_actual"])

        egresado = {
            "dni": data["dni"],
            "nombres": data["nombres"],
            "apellidos": data["apellidos"],
            "email": data["email"],
            "fecha_nac": data["fecha_nac"],
            "nacionalidad": data["nacionalidad"],
            "ciudad_natal": ciudad_natal.id if ciudad_natal else None,
            "ciudad_actual": ciudad_actual.id if ciudad_actual else None,
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

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        data = self.check_or_transform_data(request.data)
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

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
