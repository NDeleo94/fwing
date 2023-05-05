from django.urls import path

from apps.fw.api.egreso_api import *

urlEgreso = [
    path(
        "api/egresos/",
        EgresoListAPIView.as_view({"get": "list"}),
        name="egreso_list",
    ),
    path(
        "api/egresos/<int:pk>/",
        EgresoDetailAPIView.as_view({"get": "retrieve"}),
        name="egreso_detail",
    ),
]
