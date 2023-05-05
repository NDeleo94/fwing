from django.urls import path

from apps.fw.api.puesto_api import *

urlPuesto = [
    path(
        "api/puestos/",
        PuestoListAPIView.as_view({"get": "list"}),
        name="puesto_list",
    ),
    path(
        "api/puestos/<int:pk>/",
        PuestoDetailAPIView.as_view({"get": "retrieve"}),
        name="puesto_detail",
    ),
]
