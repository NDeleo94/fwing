from django.urls import path

from apps.fw.api.TituloAPI import *

urlTitulo = [
    path(
        "api/titulos/",
        TituloListAPIView.as_view({"get": "list"}),
        name="carrera_list",
    ),
    path(
        "api/titulos/<int:pk>/",
        TituloDetailAPIView.as_view({"get": "retrieve"}),
        name="carrera_detail",
    ),
]
