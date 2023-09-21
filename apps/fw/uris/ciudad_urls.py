from django.urls import path

from apps.fw.api.ciudad_api import *
from apps.fw.views.ciudad_views import CiudadView

urlCiudad = [
    path(
        "api/ciudades/",
        CiudadReadOnlyAPIView.as_view({"get": "list"}),
        name="ciudad_list",
    ),
    path(
        "api/ciudades/<int:pk>/",
        CiudadReadOnlyAPIView.as_view({"get": "retrieve"}),
        name="ciudad_detail",
    ),
    path(
        "api/crear/ciudades/",
        CiudadUpdateAPIView.as_view({"post": "create"}),
        name="ciudad_create",
    ),
    path(
        "api/editar/ciudades/<int:pk>/",
        CiudadUpdateAPIView.as_view({"put": "update"}),
        name="ciudad_update",
    ),
    path(
        "api/eliminar/ciudades/<int:pk>/",
        CiudadUpdateAPIView.as_view({"delete": "destroy"}),
        name="ciudad_delete",
    ),
    path(
        "api/ciudades/uplocation/",
        CiudadView.as_view(),
        name="locations",
    ),
]
