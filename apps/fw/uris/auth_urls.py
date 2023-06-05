from django.urls import path

from apps.fw.views.auth_views import *

urlAuth = [
    path(
        "api/login/",
        LoginView.as_view(),
        name="login",
    ),
    path(
        "api/google/",
        LoginGoogleView.as_view(),
        name="google_login",
    ),
    path(
        "api/logout/",
        LogoutView.as_view(),
        name="logout",
    ),
]
