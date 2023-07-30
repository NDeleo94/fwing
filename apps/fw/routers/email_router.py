from rest_framework import routers

from apps.fw.api.email_api import EmailAPIView

router_email = routers.DefaultRouter()

router_email.register("emails", EmailAPIView)  # GET (List, Retrieve)
