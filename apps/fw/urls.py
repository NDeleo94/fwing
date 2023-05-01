from django.urls import path

from apps.fw.uris.UniversidadURLs import urlUniversidad
from apps.fw.uris.FacultadURLs import urlFacultad
from apps.fw.uris.CarreraURLs import urlCarrera
from apps.fw.uris.TituloURLs import urlTitulo
from apps.fw.uris.OrganizacionURLs import urlOrganizacion
from apps.fw.uris.PuestoURLs import urlPuesto
from apps.fw.uris.ActividadURLs import urlActividad

urls = (
    urlUniversidad
    + urlFacultad
    + urlCarrera
    + urlTitulo
    + urlOrganizacion
    + urlPuesto
    + urlActividad
)

urlpatterns = []
