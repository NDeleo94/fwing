import requests

from apps.fw.models.ciudad_model import Ciudad

from apps.fw.serializers.ciudad_serializers import *

from decouple import config


def get_data_from_bing(ciudad):
    try:
        urlBase = config("BING_MAPS_URL")
        key = config("BING_MAPS_KEY")

        url = f"{urlBase}/{ciudad}?o=json&key={key}"

        response = requests.get(
            url=url,
        ).json()

        return response

    except requests.exceptions.RequestException as e:
        print({"error": f"Network Error: {e}"})

    except Exception as e:
        print({"error": f"An unexpected error occurred: {str(e)}"})


def check_data(data):
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

    if check_data(data=data):
        coordenadas = get_coordinates(data=data)

        set_coordinates(
            ciudad=ciudad,
            coordenadas=coordenadas,
        )


def get_or_create_ciudad(data):
    if not data:
        ciudad = None
    elif type(data) is str:
        data_cased = data.title()
        data_ciudad = {
            "ciudad": data_cased,
        }
        serializer = CiudadUpdateSerializer(data=data_ciudad)
        serializer.is_valid(raise_exception=True)
        ciudad = serializer.save()
    else:
        ciudad = Ciudad.objects.get(id=data)

    return ciudad
