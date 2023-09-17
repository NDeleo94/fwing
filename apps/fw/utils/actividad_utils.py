from apps.fw.utils.organizacion_utils import get_or_create_organizacion
from apps.fw.utils.puesto_utils import get_or_create_puesto
from apps.fw.utils.ciudad_utils import get_or_create_ciudad


def check_or_transform_data(data):
    organizacion = get_or_create_organizacion(data=data["organizacion"])

    puesto = get_or_create_puesto(data=data["puesto"])

    ciudad = get_or_create_ciudad(data=data["ciudad"])

    # Devolver actividad completo
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
