from django.urls import path

from apps.fw.views.image_views import *
from apps.fw.api.imagen_api import *

urlImage = [
    path(
        "media/images/<str:image_path>/",
        ImageView.as_view(),
        name="image_preview",
    ),
    path(
        "api/crear/imagenes/",
        ImagenUpdateAPIView.as_view({"post": "create"}),
        name="image_preview",
    ),
    path(
        "api/eliminar/imagenes/<int:pk>/",
        ImagenUpdateAPIView.as_view({"delete": "destroy"}),
        name="image_preview",
    ),
]
