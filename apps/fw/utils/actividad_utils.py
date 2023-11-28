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


def filter_actividad_query(queryset, filters):
    filtered_queryset = queryset

    estado = filters.get("estado")

    inicio = filters.get("inicio")
    fin = filters.get("fin")
    modalidad = filters.get("modalidad")
    seniority = filters.get("seniority")

    offset = filters.get("skip")
    limit = filters.get("limit")

    if estado:
        filtered_queryset = filtered_queryset.filter(estado=estado)
    else:
        filtered_queryset = filtered_queryset.filter(estado=True)

    if inicio:
        filtered_queryset = filtered_queryset.filter(inicio__icontains=inicio)
    if fin:
        filtered_queryset = filtered_queryset.filter(fin__icontains=fin)
    if modalidad:
        filtered_queryset = filtered_queryset.filter(modalidad=modalidad)
    if seniority:
        filtered_queryset = filtered_queryset.filter(seniority=seniority)

    if offset:
        filtered_queryset = filtered_queryset[int(offset) :]

    if limit:
        filtered_queryset = filtered_queryset[: int(limit)]

    return filtered_queryset
