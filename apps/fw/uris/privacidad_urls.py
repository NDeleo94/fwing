from django.urls import path

from apps.fw.api.privacidad_api import *

urlPrivacidad = [
    path(
        "api/privacidades/",
        PrivacidadAPIView.as_view({"get": "list"}),
        name="privacidad_list",
    ),
    path(
        "api/privacidades/<int:pk>/",
        PrivacidadAPIView.as_view({"get": "retrieve"}),
        name="privacidad_detail",
    ),
]
