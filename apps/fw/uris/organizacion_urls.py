from django.urls import path

from apps.fw.api.organizacion_api import *

urlOrganizacion = [
    path(
        "api/organizaciones/",
        OrganizacionReadOnlyAPIView.as_view({"get": "list"}),
        name="organizacion_list",
    ),
    path(
        "api/organizaciones/<int:pk>/",
        OrganizacionReadOnlyAPIView.as_view({"get": "retrieve"}),
        name="organizacion_detail",
    ),
    path(
        "api/crear/organizaciones/",
        OrganizacionUpdateAPIView.as_view({"post": "create"}),
        name="organizacion_create",
    ),
    path(
        "api/editar/organizaciones/<int:pk>/",
        OrganizacionUpdateAPIView.as_view({"put": "update"}),
        name="organizacion_update",
    ),
    path(
        "api/eliminar/organizaciones/<int:pk>/",
        OrganizacionUpdateAPIView.as_view({"delete": "destroy"}),
        name="organizacion_delete",
    ),
]
