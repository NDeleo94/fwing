from rest_framework import viewsets, mixins

from apps.fw.serializers.egresado_serializers import *

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

    def get_separated_data(self, data):
        egresado = {
            "dni": data["dni"],
            "nombres": data["nombres"],
            "apellidos": data["apellidos"],
            "email": data["email"],
            "fecha_nac": data["fecha_nac"],
            "nacionalidad": data["nacionalidad"],
            "ciudad_natal": data["ciudad_natal"],
            "ciudad_actual": data["ciudad_actual"],
            "sexo": data["sexo"],
        }

        egreso = {
            "carrera": data["carrera"],
            "ciclo_egreso": data["ciclo_egreso"],
        }
        return egresado, egreso

    def create(self, request, *args, **kwargs):
        egresado, egreso = self.get_separated_data(request.data)
        serializer = self.get_serializer(data=egresado)
        serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
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
