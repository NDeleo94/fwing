from rest_framework import routers

from apps.fw.api.UniversidadAPI import UniversidadAPIView
from apps.fw.api.FacultadAPI import FacultadAPIView
from apps.fw.api.CarreraAPI import CarreraAPIView
from apps.fw.api.TituloAPI import TituloAPIView
from apps.fw.api.OrganizacionAPI import OrganizacionAPIView
from apps.fw.api.PuestoAPI import PuestoAPIView
from apps.fw.api.ActividadAPI import ActividadAPIView

router = routers.DefaultRouter()

router.register("universidades", UniversidadAPIView)  # GET (List, Retrieve)
router.register("facultades", FacultadAPIView)  # GET (List, Retrieve)
router.register("carreras", CarreraAPIView)  # GET (List, Retrieve)
router.register("titulos", TituloAPIView)  # GET (List, Retrieve)
router.register("organizaciones", OrganizacionAPIView)  # GET (List, Retrieve), POST
router.register("puestos", PuestoAPIView)  # GET (List, Retrieve), POST
router.register("actividades", ActividadAPIView)  # GET (List, Retrieve), POST

urlpatterns = router.urls
