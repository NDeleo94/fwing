from rest_framework import routers

from apps.fw.api.egreso_api import EgresoAPIView

router_egreso = routers.DefaultRouter()

router_egreso.register("egresos", EgresoAPIView)  # GET (List, Retrieve), POST
