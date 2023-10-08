from apps.fw.models.privacidad_model import Privacidad

from apps.fw.serializers.privacidad_serializers import PrivacidadSerializer


def check_privacity(usuario):
    privacidad = Privacidad.objects.filter(
        usuario=usuario,
    ).first()

    if privacidad:
        return privacidad
    else:
        return False


def create_privacidad(usuario):
    data_privacidad = {
        "usuario": usuario.id,
    }
    serializer = PrivacidadSerializer(data=data_privacidad)
    serializer.is_valid(raise_exception=True)
    privacidad = serializer.save()
    return privacidad
