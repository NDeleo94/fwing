from django.urls import path

from apps.fw.api.CarreraAPI import *

urlCarrera = [
    path(
        "api/carreras/",
        CarreraListAPIView.as_view({"get": "list"}),
        name="carrera_list",
    ),
    path(
        "api/carreras/<int:pk>/",
        CarreraDetailAPIView.as_view({"get": "retrieve"}),
        name="carrera_detail",
    ),
]
