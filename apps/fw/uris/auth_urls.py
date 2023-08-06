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
    path(
        "api/new-password/",
        NewPassword.as_view(),
        name="new_password",
    ),
    path(
        "api/change-password/",
        ChangePassword.as_view(),
        name="change_password",
    ),
    path(
        "api/reset-password/",
        ResetPassword.as_view(),
        name="reset_password",
    ),
]
