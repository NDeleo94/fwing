from django.urls import path

from apps.fw.api.facultad_api import *

urlFacultad = [
    path(
        "api/facultades/",
        FacultadReadOnlyAPIView.as_view({"get": "list"}),
        name="facultad_list",
    ),
    path(
        "api/facultades/<int:pk>/",
        FacultadReadOnlyAPIView.as_view({"get": "retrieve"}),
        name="facultad_detail",
    ),
    path(
        "api/crear/facultades/",
        FacultadUpdateAPIView.as_view({"post": "create"}),
        name="facultad_create",
    ),
    path(
        "api/editar/facultades/<int:pk>/",
        FacultadUpdateAPIView.as_view({"put": "update"}),
        name="facultad_update",
    ),
    path(
        "api/eliminar/facultades/<int:pk>/",
        FacultadUpdateAPIView.as_view({"delete": "destroy"}),
        name="facultad_delete",
    ),
]
