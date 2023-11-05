from apps.fw.utils.organizacion_utils import get_or_create_organizacion
from apps.fw.utils.puesto_utils import get_or_create_puesto
from apps.fw.utils.ciudad_utils import get_or_create_ciudad, add_coordinates


def check_or_transform_data(data):
    organizacion = get_or_create_organizacion(data=data.get("organizacion"))

    puesto = get_or_create_puesto(data=data.get("puesto"))

    ciudad = get_or_create_ciudad(data=data.get("ciudad"))

    if ciudad:
        try:
            add_coordinates(ciudad=ciudad)
        except Exception as e:
            print({"error": f"An unexpected error occurred: {str(e)}"})

    data_transformed = {
        "inicio": data.get("inicio"),
        "fin": data.get("fin"),
        "usuario": data.get("usuario"),
        "organizacion": organizacion.id,
        "puesto": puesto.id,
        "ciudad": ciudad.id if ciudad else None,
        "modalidad": data.get("modalidad"),
        "seniority": data.get("seniority"),
    }
    return data_transformed
