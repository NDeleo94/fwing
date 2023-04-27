from django.urls import path

from apps.fw.api.OrganizacionAPI import *

urlOrganizacion = [
    path(
        "api/organizaciones/",
        OrganizacionListAPIView.as_view({"get": "list"}),
        name="organizacion_list",
    ),
    path(
        "api/organizaciones/<int:pk>/",
        OrganizacionDetailAPIView.as_view({"get": "retrieve"}),
        name="organizacion_detail",
    ),
]
