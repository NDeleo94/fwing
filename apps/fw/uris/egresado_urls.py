from django.urls import path

from apps.fw.api.egresado_api import *

urlEgresado = [
    path(
        "api/egresados/",
        EgresadoAPIView.as_view({"get": "list"}),
        name="egresado_list",
    ),
    path(
        "api/egresados/<int:pk>/",
        EgresadoAPIView.as_view({"get": "retrieve"}),
        name="egresado_detail",
    ),
    path(
        "api/egresados/<int:pk>/",
        EgresadoAPIView.as_view({"put": "update"}),
        name="egresado_update",
    ),
]
