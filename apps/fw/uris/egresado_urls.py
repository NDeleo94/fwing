from django.urls import path

from apps.fw.api.egresado_api import *

urlEgresado = [
    path(
        "api/egresados/",
        EgresadoReadOnlyAPIView.as_view({"get": "list"}),
        name="egresado_list",
    ),
    path(
        "api/egresados/<int:pk>/",
        EgresadoReadOnlyAPIView.as_view({"get": "retrieve"}),
        name="egresado_detail",
    ),
    path(
        "api/crear/egresados/",
        EgresadoUpdateAPIView.as_view({"post": "create"}),
        name="egresado_create",
    ),
    path(
        "api/editar/egresados/<int:pk>/",
        EgresadoUpdateAPIView.as_view({"put": "update"}),
        name="egresado_update",
    ),
    path(
        "api/eliminar/egresados/<int:pk>/",
        EgresadoUpdateAPIView.as_view({"delete": "destroy"}),
        name="egresado_delete",
    ),
]
