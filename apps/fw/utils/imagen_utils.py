from apps.fw.models.imagen_model import Imagen

from google.auth import jwt


def check_profile_picture(usuario):
    imagen = Imagen.objects.filter(
        usuario=usuario,
        perfil=True,
    ).first()

    if imagen:
        return imagen
    else:
        return False


def get_google_property(token, property):
    try:
        decoded_token = jwt.decode(token, verify=False)
        google_email = decoded_token.get(property)
        return google_email
    except jwt.exceptions.DecodeError as e:
        print(f"Error decoding Google token: {e}")
        return None


def check_or_transform_data(data):
    if data["file"]:
        file = data["file"]
        url = None
    else:
        file = None
        url = get_google_property(data["url"], "picture")

    data_transformed = {
        "usuario": data["usuario"],
        "file": file,
        "url": url,
        "perfil": True,
        "estado": True,
    }
    return data_transformed
