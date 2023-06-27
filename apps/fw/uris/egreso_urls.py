from django.urls import path

from apps.fw.api.egreso_api import *

urlEgreso = [
    path(
        "api/egresos/",
        EgresoReadOnlyAPIView.as_view({"get": "list"}),
        name="egreso_list",
    ),
    path(
        "api/egresos/<int:pk>/",
        EgresoReadOnlyAPIView.as_view({"get": "retrieve"}),
        name="egreso_detail",
    ),
    path(
        "api/crear/egresos/",
        EgresoUpdateAPIView.as_view({"post": "create"}),
        name="egreso_create",
    ),
    path(
        "api/editar/egresos/<int:pk>/",
        EgresoUpdateAPIView.as_view({"put": "update"}),
        name="egreso_update",
    ),
    path(
        "api/eliminar/egresos/<int:pk>/",
        EgresoUpdateAPIView.as_view({"delete": "destroy"}),
        name="egreso_delete",
    ),
]
