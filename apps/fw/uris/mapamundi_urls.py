from django.urls import path

from apps.fw.api.mapamundi_api import *

urlMapaMundi = [
    path(
        "api/mapamundi/",
        ActividadMapaMundiAPIView.as_view({"get": "list"}),
        name="actividades_mapamundi_list",
    ),
]
