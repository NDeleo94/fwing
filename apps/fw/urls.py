from django.urls import path

from apps.fw.uris.universidad_urls import urlUniversidad
from apps.fw.uris.facultad_urls import urlFacultad
from apps.fw.uris.carrera_urls import urlCarrera
from apps.fw.uris.titulo_urls import urlTitulo
from apps.fw.uris.organizacion_urls import urlOrganizacion
from apps.fw.uris.puesto_urls import urlPuesto
from apps.fw.uris.actividad_urls import urlActividad
from apps.fw.uris.egreso_urls import urlEgreso
from apps.fw.uris.egresado_urls import urlEgresado
from apps.fw.uris.auth_urls import urlAuth

urls = (
    urlUniversidad
    + urlFacultad
    + urlCarrera
    + urlTitulo
    + urlOrganizacion
    + urlPuesto
    + urlActividad
    + urlEgreso
    + urlEgresado
)

urlpatterns = urlAuth
