from django.urls import path

from apps.fw.api.actividad_api import *

urlActividad = [
    path(
        "api/actividades/",
        ActividadReadOnlyAPIView.as_view({"get": "list"}),
        name="actividad_list",
    ),
    path(
        "api/actividades/<int:pk>/",
        ActividadReadOnlyAPIView.as_view({"get": "retrieve"}),
        name="actividad_detail",
    ),
    path(
        "api/crear/actividades/",
        ActividadUpdateAPIView.as_view({"post": "create"}),
        name="actividad_create",
    ),
    path(
        "api/editar/actividades/<int:pk>/",
        ActividadUpdateAPIView.as_view({"put": "update"}),
        name="actividad_update",
    ),
    path(
        "api/eliminar/actividades/<int:pk>/",
        ActividadUpdateAPIView.as_view({"delete": "destroy"}),
        name="actividad_delete",
    ),
]
