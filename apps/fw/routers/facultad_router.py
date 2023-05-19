from rest_framework import routers

from apps.fw.api.facultad_api import FacultadAPIView

router_facultad = routers.DefaultRouter()

router_facultad.register("facultades", FacultadAPIView)  # GET (List, Retrieve)
