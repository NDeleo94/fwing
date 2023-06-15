from django.urls import path

from apps.fw.views.image_views import *

urlImage = [
    path(
        "media/images/<str:image_path>/",
        ImageView.as_view(),
        name="image_preview",
    ),
]
