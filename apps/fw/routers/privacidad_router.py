from rest_framework import routers

from apps.fw.api.privacidad_api import PrivacidadAPIView

router_privacidad = routers.DefaultRouter()

router_privacidad.register("privacidades", PrivacidadAPIView)
