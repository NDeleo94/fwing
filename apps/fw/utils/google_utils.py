from apps.fw.models.imagen_model import Imagen
from apps.fw.serializers.imagen_serializers import *

from google.auth import jwt


def get_google_property(token, property):
    try:
        decoded_token = jwt.decode(token, verify=False)
        google_email = decoded_token.get(property)
        return google_email
    except jwt.exceptions.DecodeError as e:
        print(f"Error decoding Google token: {e}")
        return None


def set_google_profile_picture(usuario, token):
    imagen = Imagen.objects.filter(usuario=usuario).first()
    if imagen:
        imagen.url = get_google_property(token, "picture")
        imagen.file = None
        imagen.save()
    else:
        data_imagen = {
            "usuario": usuario.id,
            "file": None,
            "url": get_google_property(token, "picture"),
        }
        serializer = ImagenSerializer(data=data_imagen)
        serializer.is_valid(raise_exception=True)
        serializer.save()
