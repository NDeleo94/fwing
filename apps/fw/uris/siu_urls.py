from django.urls import path

from apps.fw.views.siu_views import *

urlSIU = [
    path(
        "api/siu/",
        EgresadosSIU.as_view(),
        name="siu",
    ),
]
