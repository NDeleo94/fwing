from rest_framework import viewsets, mixins

from apps.fw.serializers.egreso_serializers import *

from apps.fw.utils.egreso_utils import check_or_transform_data

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

    def create(self, request, *args, **kwargs):
        data = check_or_transform_data(request.data)
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
        data = check_or_transform_data(request.data)
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
