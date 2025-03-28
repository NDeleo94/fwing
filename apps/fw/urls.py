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
from apps.fw.uris.privacidad_urls import urlPrivacidad
from apps.fw.uris.auth_urls import urlAuth
from apps.fw.uris.siu_urls import urlSIU
from apps.fw.uris.image_urls import urlImage
from apps.fw.uris.email_urls import urlEmail
from apps.fw.uris.ciudad_urls import urlCiudad
from apps.fw.uris.linkedin_urls import urlLinkedin
from apps.fw.uris.mapamundi_urls import urlMapaMundi
from apps.fw.uris.test_urls import urlTest

urls = urlTitulo

urlpatterns = (
    urlAuth
    + urlSIU
    + urlImage
    + urlEgresado
    + urlEgreso
    + urlUniversidad
    + urlFacultad
    + urlCarrera
    + urlOrganizacion
    + urlPuesto
    + urlActividad
    + urlEmail
    + urlPrivacidad
    + urlCiudad
    + urlLinkedin
    + urlMapaMundi
    + urlTest
)
