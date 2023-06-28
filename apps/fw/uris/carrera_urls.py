from django.urls import path

from apps.fw.api.carrera_api import *

urlCarrera = [
    path(
        "api/carreras/",
        CarreraReadOnlyAPIView.as_view({"get": "list"}),
        name="carrera_list",
    ),
    path(
        "api/carreras/<int:pk>/",
        CarreraReadOnlyAPIView.as_view({"get": "retrieve"}),
        name="carrera_detail",
    ),
    path(
        "api/crear/carreras/",
        CarreraUpdateAPIView.as_view({"post": "create"}),
        name="carrera_create",
    ),
    path(
        "api/editar/carreras/<int:pk>/",
        CarreraUpdateAPIView.as_view({"put": "update"}),
        name="carrera_update",
    ),
    path(
        "api/eliminar/carreras/<int:pk>/",
        CarreraUpdateAPIView.as_view({"delete": "destroy"}),
        name="carrera_delete",
    ),
]
