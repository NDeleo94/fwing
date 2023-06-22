from rest_framework import routers
from apps.fw.routers.universidad_router import router_universidad
from apps.fw.routers.facultad_router import router_facultad
from apps.fw.routers.carrera_router import router_carrera
from apps.fw.routers.titulo_router import router_titulo
from apps.fw.routers.organizacion_router import router_organizacion
from apps.fw.routers.puesto_router import router_puesto
from apps.fw.routers.actividad_router import router_actividad
from apps.fw.routers.egreso_router import router_egreso
from apps.fw.routers.egresado_router import router_egresado
from apps.fw.routers.privacidad_router import router_privacidad

router = routers.DefaultRouter()

router.registry.extend(router_universidad.registry)
router.registry.extend(router_facultad.registry)
router.registry.extend(router_carrera.registry)
router.registry.extend(router_titulo.registry)
router.registry.extend(router_organizacion.registry)
router.registry.extend(router_puesto.registry)
router.registry.extend(router_actividad.registry)
router.registry.extend(router_egreso.registry)
router.registry.extend(router_egresado.registry)
router.registry.extend(router_privacidad.registry)

urlpatterns = router.urls
