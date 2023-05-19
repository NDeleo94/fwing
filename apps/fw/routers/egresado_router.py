from rest_framework import routers

from apps.fw.api.egresado_api import EgresadoAPIView

router_egresado = routers.DefaultRouter()

router_egresado.register("egresados", EgresadoAPIView)  # GET (List, Retrieve)
