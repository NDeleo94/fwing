from rest_framework import serializers

from apps.fw.models.actividad_model import Actividad
from apps.fw.models.user_model import FwUser
from apps.fw.models.organizacion_model import Organizacion
from apps.fw.models.puesto_model import Puesto
from apps.fw.models.ciudad_model import Ciudad
from apps.fw.models.imagen_model import Imagen


class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = "__all__"


class PuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puesto
        fields = (
            "id",
            "puesto",
        )


class OrganizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizacion
        fields = (
            "id",
            "organizacion",
        )


class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = (
            "id",
            "ciudad",
        )


class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = (
            "id",
            "file",
            "url",
            "perfil",
        )


class EgresadoSerializer(serializers.ModelSerializer):
    imagen = serializers.SerializerMethodField(method_name="get_profile_picture")

    class Meta:
        model = FwUser
        fields = (
            "id",
            "apellidos",
            "nombres",
            "imagen",
        )

    def get_profile_picture(self, obj):
        imagenes_queryset = obj.imagen.filter(estado=True, perfil=True).first()

        imagen_serializer = ImagenSerializer(imagenes_queryset, many=False)

        return imagen_serializer.data


class ActividadMapaMundiSerializer(serializers.ModelSerializer):
    usuario = EgresadoSerializer()
    organizacion = OrganizacionSerializer()
    puesto = PuestoSerializer()
    ciudad = CiudadSerializer()

    class Meta:
        model = Actividad
        exclude = ("estado",)
