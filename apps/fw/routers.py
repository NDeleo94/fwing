from rest_framework import routers

from apps.fw.api.UniversidadAPI import UniversidadAPIView
from apps.fw.api.FacultadAPI import FacultadAPIView

router = routers.DefaultRouter()

router.register("universidades", UniversidadAPIView)  # GET (List, Retrieve)
router.register("facultades", FacultadAPIView)  # GET (List, Retrieve)

urlpatterns = router.urls
