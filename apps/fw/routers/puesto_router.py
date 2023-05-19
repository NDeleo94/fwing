from rest_framework import routers

from apps.fw.api.puesto_api import PuestoAPIView

router_puesto = routers.DefaultRouter()

router_puesto.register("puestos", PuestoAPIView)  # GET (List, Retrieve), POST
