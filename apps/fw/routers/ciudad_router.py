from rest_framework import routers

from apps.fw.api.ciudad_api import CiudadAPIView

router_ciudad = routers.DefaultRouter()

router_ciudad.register("ciudades", CiudadAPIView)  # GET (List, Retrieve)
