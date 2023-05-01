from django.urls import path

from apps.fw.api.ActividadAPI import *

urlActividad = [
    path(
        "api/actividades/",
        ActividadListAPIView.as_view({"get": "list"}),
        name="actividad_list",
    ),
    path(
        "api/actividades/<int:pk>/",
        ActividadDetailAPIView.as_view({"get": "retrieve"}),
        name="actividad_detail",
    ),
]
