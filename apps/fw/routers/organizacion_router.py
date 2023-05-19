from rest_framework import routers

from apps.fw.api.organizacion_api import OrganizacionAPIView

router_organizacion = routers.DefaultRouter()

router_organizacion.register(
    "organizaciones", OrganizacionAPIView
)  # GET (List, Retrieve), POST
