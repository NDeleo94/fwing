from rest_framework import routers

from apps.fw.api.actividad_api import ActividadAPIView

router_actividad = routers.DefaultRouter()

router_actividad.register("actividades", ActividadAPIView)  # GET (List, Retrieve), POST
