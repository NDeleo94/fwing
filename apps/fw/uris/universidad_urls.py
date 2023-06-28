from django.urls import path

from apps.fw.api.universidad_api import *

urlUniversidad = [
    path(
        "api/universidades/",
        UniversidadReadOnlyAPIView.as_view({"get": "list"}),
        name="universidad_list",
    ),
    path(
        "api/universidades/<int:pk>/",
        UniversidadReadOnlyAPIView.as_view({"get": "retrieve"}),
        name="universidad_detail",
    ),
    path(
        "api/crear/universidades/",
        UniversidadUpdateAPIView.as_view({"post": "create"}),
        name="universidad_create",
    ),
    path(
        "api/editar/universidades/<int:pk>/",
        UniversidadUpdateAPIView.as_view({"put": "update"}),
        name="universidad_update",
    ),
    path(
        "api/eliminar/universidades/<int:pk>/",
        UniversidadUpdateAPIView.as_view({"delete": "destroy"}),
        name="universidad_delete",
    ),
]
