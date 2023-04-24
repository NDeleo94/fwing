from rest_framework import routers

from apps.fw.api.UniversidadAPI import UniversidadAPIView

router = routers.DefaultRouter()

router.register("universidades", UniversidadAPIView)  # GET (List, Retrieve)

urlpatterns = router.urls
