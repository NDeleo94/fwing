from django.urls import path

from apps.fw.api.facultad_api import *

urlFacultad = [
    path(
        "api/facultades/",
        FacultadListAPIView.as_view({"get": "list"}),
        name="facultad_list",
    ),
    path(
        "api/facultades/<int:pk>/",
        FacultadDetailAPIView.as_view({"get": "retrieve"}),
        name="facultad_detail",
    ),
]
