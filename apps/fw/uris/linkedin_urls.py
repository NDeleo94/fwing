from django.urls import path

from apps.fw.views.linkedin_views import *

urlLinkedin = [
    path(
        "api/linkedin/",
        LinkedInView.as_view(),
        name="linkedin",
    ),
]
