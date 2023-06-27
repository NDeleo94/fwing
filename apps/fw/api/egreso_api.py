from rest_framework import viewsets, mixins

from apps.fw.serializers.egreso_serializers import *

from apps.fw.models.universidad_model import Universidad
from apps.fw.models.facultad_model import Facultad
from apps.fw.models.carrera_model import Carrera

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class EgresoUpdateAPIView(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Egreso.objects.all()
    serializer_class = EgresoUpdateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_or_create_universidad(self, data):
        if type(data) is str:
            universidad = Universidad.objects.create(
                universidad=data,
            )
        else:
            universidad = Universidad.objects.get(
                id=data,
            )
        return universidad

    def get_or_create_facultad(self, data, universidad):
        if type(data) is str:
            facultad = Facultad.objects.create(
                facultad=data,
                universidad=universidad,
            )
        else:
            facultad = Facultad.objects.get(
                id=data,
            )
        return facultad

    def get_or_create_carrera(self, data, facultad):
        if type(data) is str:
            carrera = Carrera.objects.create(
                carrera=data,
                facultad=facultad,
            )
        else:
            carrera = Carrera.objects.get(
                id=data,
            )
        return carrera

    def check_or_transform_data(self, data):
        universidad = self.get_or_create_universidad(
            data=data["universidad"],
        )
        facultad = self.get_or_create_facultad(
            data=data["facultad"],
            universidad=universidad,
        )
        carrera = self.get_or_create_carrera(
            data=data["carrera"],
            facultad=facultad,
        )

        data_transformed = {
            "universidad": universidad.id,
            "facultad": facultad.id,
            "carrera": carrera.id,
            "ciclo_egreso": data["ciclo_egreso"],
            "matricula": data["matricula"],
            "usuario": data["usuario"],
        }

        return data_transformed

    def create(self, request, *args, **kwargs):
        data = self.check_or_transform_data(request.data)
        serializer = self.get_serializer(data=data)
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
        instance.estado = False
        instance.save()
        return Response(
            {"message": "Egreso deleted"},
            status=status.HTTP_200_OK,
        )


class EgresoReadOnlyAPIView(
    viewsets.ReadOnlyModelViewSet,
):
    queryset = Egreso.objects.filter(estado=True).order_by(
        "carrera",
        "ciclo_egreso",
    )
    serializer_class = EgresoReadOnlySerializer


class EgresoAPIView(viewsets.ModelViewSet):
    serializer_class = EgresoSerializer
    queryset = serializer_class.Meta.model.objects.filter(estado=True)

    def get_serializer_class(self):
        if self.action in ["create", "update"]:
            return EgresoSerializer
        return EgresoReadOnlySerializer
