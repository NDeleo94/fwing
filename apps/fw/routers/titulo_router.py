from rest_framework import routers

from apps.fw.api.titulo_api import TituloAPIView

router_titulo = routers.DefaultRouter()

router_titulo.register("titulos", TituloAPIView)  # GET (List, Retrieve)
