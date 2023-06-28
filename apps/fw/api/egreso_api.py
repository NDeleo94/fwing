from rest_framework import viewsets, mixins

from apps.fw.serializers.egreso_serializers import *
from apps.fw.serializers.universidad_serializers import *
from apps.fw.serializers.facultad_serializers import *
from apps.fw.serializers.carrera_serializers import *

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
            data_cased = data.title()
            data_universidad = {
                "universidad": data_cased,
            }
            serializer = UniversidadUpdateSerializer(data=data_universidad)
            serializer.is_valid(raise_exception=True)
            universidad = serializer.save()
        else:
            universidad = Universidad.objects.get(id=data)

        return universidad

    def get_or_create_facultad(self, data, universidad):
        if type(data) is str:
            data_cased = data.title()
            data_facultad = {
                "facultad": data_cased,
                "universidad": universidad,
            }
            serializer = FacultadUpdateSerializer(data=data_facultad)
            serializer.is_valid(raise_exception=True)
            facultad = serializer.save()
        else:
            facultad = Facultad.objects.get(id=data)

        return facultad

    def get_or_create_carrera(self, data, facultad):
        if type(data) is str:
            data_cased = data.title()
            data_carrera = {
                "carrera": data_cased,
                "facultad": facultad,
            }
            serializer = CarreraUpdateSerializer(data=data_carrera)
            serializer.is_valid(raise_exception=True)
            carrera = serializer.save()
        else:
            carrera = Carrera.objects.get(id=data)

        return carrera

    def check_or_transform_data(self, data):
        universidad = self.get_or_create_universidad(
            data=data["universidad"],
        )
        facultad = self.get_or_create_facultad(
            data=data["facultad"],
            universidad=universidad.id,
        )
        carrera = self.get_or_create_carrera(
            data=data["carrera"],
            facultad=facultad.id,
        )

        data_transformed = {
            "universidad": universidad.id,
            "facultad": facultad.id,
            "carrera": carrera.id,
            "usuario": data["usuario"],
            "ciclo_egreso": data["ciclo_egreso"],
            "matricula": data["matricula"],
        }

        return data_transformed

    def create(self, request, *args, **kwargs):
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
