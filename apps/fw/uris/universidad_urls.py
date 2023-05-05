from django.urls import path

from apps.fw.api.universidad_api import *

urlUniversidad = [
    path(
        "api/universidades/",
        UniversidadListAPIView.as_view({"get": "list"}),
        name="university_list",
    ),
    path(
        "api/universidades/<int:pk>/",
        UniversidadDetailAPIView.as_view({"get": "retrieve"}),
        name="university_detail",
    ),
]
