from rest_framework import routers

from apps.fw.api.imagen_api import ImagenAPIView

router_imagen = routers.DefaultRouter()

router_imagen.register("imagenes", ImagenAPIView)  # GET (List, Retrieve)
