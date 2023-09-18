from django.urls import path

from apps.fw.views.test_views import *

urlTest = [
    path(
        "api/test/",
        TestView.as_view(),
        name="test",
    ),
]
