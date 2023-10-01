from django.urls import path

from apps.fw.views.siu_views import *
from apps.fw.api.log_siu_api import *

urlSIU = [
    path(
        "api/siu/",
        EgresadosSIU.as_view(),
        name="siu",
    ),
    path(
        "api/log/",
        LogSIUAPIView.as_view({"get": "list"}),
        name="log_siu",
    ),
]
