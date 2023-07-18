from rest_framework import serializers

from apps.fw.models.user_model import FwUser
from apps.fw.models.egreso_model import Egreso
from apps.fw.models.carrera_model import Carrera
from apps.fw.models.facultad_model import Facultad
from apps.fw.models.universidad_model import Universidad
from apps.fw.models.actividad_model import Actividad
from apps.fw.models.organizacion_model import Organizacion
from apps.fw.models.puesto_model import Puesto
from apps.fw.models.imagen_model import Imagen
from apps.fw.models.privacidad_model import Privacidad


# Serializers base para lista de egresos
class UniversidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universidad
        fields = (
            "id",
            "universidad",
            "acronimo",
        )


class FacultadSerializer(serializers.ModelSerializer):
    universidad = UniversidadSerializer()

    class Meta:
        model = Facultad
        fields = (
            "id",
            "facultad",
            "acronimo",
            "universidad",
        )


class CarreraSerializer(serializers.ModelSerializer):
    facultad = FacultadSerializer()

    class Meta:
        model = Carrera
        fields = (
            "id",
            "carrera",
            "facultad",
        )


class EgresoSerializer(serializers.ModelSerializer):
    carrera = CarreraSerializer()

    class Meta:
        model = Egreso
        fields = (
            "id",
            "ciclo_egreso",
            "matricula",
            "postgrado",
            "carrera",
        )


# Serializers base para lista de actividades
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
            "tipo",
            "empleados",
        )


class ActividadSerializer(serializers.ModelSerializer):
    organizacion = OrganizacionSerializer()
    puesto = PuestoSerializer()

    class Meta:
        model = Actividad
        fields = (
            "id",
            "inicio",
            "fin",
            "modalidad",
            "seniority",
            "organizacion",
            "puesto",
        )


# Serializers base para lista de imagenes
class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = (
            "id",
            "file",
            "url",
            "perfil",
        )


# Serializers base para privacidad
class PrivacidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Privacidad
        exclude = ("usuario",)


# Serializer de solo lectura Egresado
class EgresadoReadOnlySerializer(serializers.ModelSerializer):
    egresos = serializers.SerializerMethodField(method_name="get_egresos")
    historial = serializers.SerializerMethodField(method_name="get_historial")
    imagen = serializers.SerializerMethodField(method_name="get_profile_picture")
    privacidad = PrivacidadSerializer()

    class Meta:
        model = FwUser
        fields = (
            "id",
            "dni",
            "apellidos",
            "nombres",
            "email",
            "nacionalidad",
            "fecha_nac",
            "ciudad_natal",
            "ciudad_actual",
            "domicilio",
            "certificado",
            "sexo",
            "last_login",
            "is_admin",
            "egresos",
            "historial",
            "imagen",
            "privacidad",
        )

    def get_egresos(self, obj):
        egresos_queryset = obj.egresos.filter(estado=True)

        egreso_serializer = EgresoSerializer(egresos_queryset, many=True)

        return egreso_serializer.data

    def get_historial(self, obj):
        actividades_queryset = obj.historial.filter(estado=True)

        actividad_serializer = ActividadSerializer(actividades_queryset, many=True)

        return actividad_serializer.data

    def get_profile_picture(self, obj):
        imagenes_queryset = obj.imagen.filter(estado=True, perfil=True)

        imagen_serializer = ImagenSerializer(imagenes_queryset, many=True)

        return imagen_serializer.data


# Serializer de actualizacion Egresado
class EgresadoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FwUser
        fields = (
            "dni",
            "apellidos",
            "nombres",
            "email",
            "nacionalidad",
            "fecha_nac",
            "ciudad_natal",
            "ciudad_actual",
            "sexo",
            "is_admin",
        )


class EgresadoLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = FwUser
        fields = (
            "id",
            "dni",
            "apellidos",
            "nombres",
            "email",
            "nacionalidad",
            "fecha_nac",
            "ciudad_natal",
            "ciudad_actual",
            "domicilio",
            "certificado",
            "sexo",
            "is_admin",
            "last_login",
        )
