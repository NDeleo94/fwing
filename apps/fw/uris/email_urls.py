from django.urls import path

from apps.fw.views.email_views import *

urlEmail = [
    path(
        "api/email/",
        EmailView.as_view(),
        name="email_invitation",
    ),
]
