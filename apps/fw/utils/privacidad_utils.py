from apps.fw.models.privacidad_model import Privacidad


def check_privacity(usuario):
    privacidad = Privacidad.objects.filter(
        usuario=usuario,
    ).first()

    if privacidad:
        return privacidad
    else:
        return False
