from rest_framework import routers

from apps.fw.api.universidad_api import UniversidadAPIView
from apps.fw.api.facultad_api import FacultadAPIView
from apps.fw.api.carrera_api import CarreraAPIView
from apps.fw.api.titulo_api import TituloAPIView
from apps.fw.api.organizacion_api import OrganizacionAPIView
from apps.fw.api.puesto_api import PuestoAPIView
from apps.fw.api.actividad_api import ActividadAPIView
from apps.fw.api.egreso_api import EgresoAPIView

router = routers.DefaultRouter()

router.register("universidades", UniversidadAPIView)  # GET (List, Retrieve)
router.register("facultades", FacultadAPIView)  # GET (List, Retrieve)
router.register("carreras", CarreraAPIView)  # GET (List, Retrieve)
router.register("titulos", TituloAPIView)  # GET (List, Retrieve)
router.register("organizaciones", OrganizacionAPIView)  # GET (List, Retrieve), POST
router.register("puestos", PuestoAPIView)  # GET (List, Retrieve), POST
router.register("actividades", ActividadAPIView)  # GET (List, Retrieve), POST
router.register("egresos", EgresoAPIView)  # GET (List, Retrieve), POST

urlpatterns = router.urls
