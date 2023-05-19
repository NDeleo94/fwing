from rest_framework import routers

from apps.fw.api.universidad_api import UniversidadAPIView

router_universidad = routers.DefaultRouter()

router_universidad.register("universidades", UniversidadAPIView)  # GET (List, Retrieve)
