from django.urls import path

from apps.fw.api.privacidad_api import *

urlPrivacidad = [
    path(
        "api/crear/privacidades/",
        PrivacidadUpdateAPIView.as_view({"post": "create"}),
        name="privacidad_update",
    ),
]
