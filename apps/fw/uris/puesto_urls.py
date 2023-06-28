from django.urls import path

from apps.fw.api.puesto_api import *

urlPuesto = [
    path(
        "api/puestos/",
        PuestoReadOnlyAPIView.as_view({"get": "list"}),
        name="puesto_list",
    ),
    path(
        "api/puestos/<int:pk>/",
        PuestoReadOnlyAPIView.as_view({"get": "retrieve"}),
        name="puesto_detail",
    ),
    path(
        "api/crear/puestos/",
        PuestoUpdateAPIView.as_view({"post": "create"}),
        name="puesto_create",
    ),
    path(
        "api/editar/puestos/<int:pk>/",
        PuestoUpdateAPIView.as_view({"put": "update"}),
        name="puesto_update",
    ),
    path(
        "api/eliminar/puestos/<int:pk>/",
        PuestoUpdateAPIView.as_view({"delete": "destroy"}),
        name="puesto_delete",
    ),
]
