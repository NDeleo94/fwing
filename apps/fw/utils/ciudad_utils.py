import requests

from apps.fw.models.ciudad_model import Ciudad

from apps.fw.serializers.ciudad_serializers import *

from decouple import config


def get_data_from_bing(ciudad):
    urlBase = config("BING_MAPS_URL")
    key = config("BING_MAPS_KEY")

    url = f"{urlBase}/{ciudad}?o=json&key={key}"

    response = requests.get(
        url=url,
    ).json()

    return response


def check_data_from_bing(data):
    results = data.get("resourceSets")[0].get("estimatedTotal")

    return results


def get_coordinates(data):
    coordenadas = (
        data.get("resourceSets")[0]
        .get("resources")[0]
        .get("geocodePoints")[0]
        .get("coordinates")
    )

    return coordenadas


def set_coordinates(ciudad, coordenadas):
    lat, long = coordenadas

    ciudad.lat = lat
    ciudad.long = long
    ciudad.save()


def add_coordinates(ciudad):
    data = get_data_from_bing(ciudad=ciudad.ciudad)

    if check_data_from_bing(data=data):
        coordenadas = get_coordinates(data=data)

        set_coordinates(
            ciudad=ciudad,
            coordenadas=coordenadas,
        )


def create_ciudad(data):
    data_cased = data.title()
    data_ciudad = {
        "ciudad": data_cased,
    }
    serializer = CiudadUpdateSerializer(data=data_ciudad)
    serializer.is_valid(raise_exception=True)
    ciudad = serializer.save()
    return ciudad


def get_ciudad(data):
    if not data:
        ciudad = None
    elif type(data) is str:
        ciudad = Ciudad.objects.filter(ciudad__icontains=data).first()
    else:
        ciudad = Ciudad.objects.get(id=data)

    return ciudad


def get_or_create_ciudad(data):
    ciudad = get_ciudad(data=data)

    if not ciudad:
        ciudad = create_ciudad(data=data)
        add_coordinates(ciudad=ciudad)

    return ciudad


def fetch_ciudades():
    return Ciudad.objects.all()


def set_city_on_row(row, key):
    try:
        row[key] = get_or_create_ciudad(row[key])
    except Exception as e:
        print(e)

    return row


def filter_query(queryset, filters):
    filtered_queryset = queryset

    ciudad = filters.get("ciudad")
    offset = filters.get("skip")
    limit = filters.get("limit")

    if ciudad:
        filtered_queryset = filtered_queryset.filter(ciudad__icontains=ciudad)

    if offset:
        filtered_queryset = filtered_queryset[int(offset) :]

    if limit:
        filtered_queryset = filtered_queryset[: int(limit)]

    return filtered_queryset
