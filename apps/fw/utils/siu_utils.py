import requests, base64

from apps.fw.models.log_siu_model import LogSIU

from decouple import config


def register_update(cantidad, origen):
    log_entry = LogSIU.objects.create(cantidad=cantidad, origen=origen)

    return log_entry


def get_credentials():
    user = config("SIU_FACET_USER")
    password = config("SIU_FACET_PASSWORD")

    credentials = f"{user}:{password}"

    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    return encoded_credentials


def flat_data_from_SIU(data: list):
    return [egresado["post"] for egresado in data]


def get_egresados_from_SIU():
    encoded_credentials = get_credentials()

    response = (
        requests.get(
            url=config("SIU_FACET_URL"),
            headers={"Authorization": f"Basic {encoded_credentials}"},
        )
        .json()
        .get("data")
    )

    egresados = flat_data_from_SIU(response)

    return egresados
