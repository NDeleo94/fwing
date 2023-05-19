from rest_framework import routers

from apps.fw.api.carrera_api import CarreraAPIView

router_carrera = routers.DefaultRouter()

router_carrera.register("carreras", CarreraAPIView)  # GET (List, Retrieve)
