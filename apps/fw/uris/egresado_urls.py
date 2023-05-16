from django.urls import path

from apps.fw.api.egresado_api import *

urlEgresado = [
    path(
        "api/egresados/",
        EgresadoListSerializer.as_view({"get": "list"}),
        name="egresado_list",
    ),
    path(
        "api/egresados/<int:pk>/",
        EgresadoDetailSerializer.as_view({"get": "retrieve"}),
        name="egresado_detail",
    ),
]
