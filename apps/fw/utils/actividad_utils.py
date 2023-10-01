from apps.fw.utils.organizacion_utils import get_or_create_organizacion
from apps.fw.utils.puesto_utils import get_or_create_puesto
from apps.fw.utils.ciudad_utils import get_or_create_ciudad, add_coordinates


def check_or_transform_data(data):
    organizacion = get_or_create_organizacion(data=data["organizacion"])

    puesto = get_or_create_puesto(data=data["puesto"])

    ciudad = get_or_create_ciudad(data=data["ciudad"])

    if ciudad:
        try:
            add_coordinates(ciudad=ciudad)
        except Exception as e:
            print({"error": f"An unexpected error occurred: {str(e)}"})

    data_transformed = {
        "inicio": data["inicio"],
        "fin": data["fin"],
        "usuario": data["usuario"],
        "organizacion": organizacion.id,
        "puesto": puesto.id,
        "ciudad": ciudad.id if ciudad else None,
        "modalidad": data["modalidad"],
        "seniority": data["seniority"],
    }
    return data_transformed
