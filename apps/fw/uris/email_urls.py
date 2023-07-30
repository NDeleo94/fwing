from django.urls import path

from apps.fw.api.email_api import *
from apps.fw.views.email_views import *

urlEmail = [
    path(
        "api/email/",
        EmailReadOnlyAPIView.as_view({"get": "list"}),
        name="email_list",
    ),
    path(
        "api/email/<int:pk>/",
        EmailReadOnlyAPIView.as_view({"get": "retrieve"}),
        name="email_detail",
    ),
    path(
        "api/crear/email/",
        EmailUpdateAPIView.as_view({"post": "create"}),
        name="email_create",
    ),
    path(
        "api/editar/email/<int:pk>/",
        EmailUpdateAPIView.as_view({"put": "update"}),
        name="email_update",
    ),
    path(
        "api/eliminar/email/<int:pk>/",
        EmailUpdateAPIView.as_view({"delete": "destroy"}),
        name="email_delete",
    ),
    path(
        "api/enviar/email/",
        EmailTemplateView.as_view(),
        name="email_send_template",
    ),
    path(
        "api/email/",
        EmailView.as_view(),
        name="email_invitation",
    ),
]
