from django.contrib import admin

from apps.fw.models.privacidad_model import Privacidad

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class PuestoResources(resources.ModelResource):
    class Meta:
        model = Privacidad
        fields = (
            "id",
            "dni",
            "email",
            "nombres",
            "apellidos",
            "fecha_nac",
            "nacionalidad",
            "ciudad_natal",
            "ciudad_actual",
            "domicilio",
            "certificado",
            "sexo",
            "usuario",
        )


# Esta clase hereda de admin.ModelAdmin
class PrivacidadImportExportAdmin(ImportExportModelAdmin):
    resource_classes = [PuestoResources]


@admin.register(Privacidad)
class PrivacidadAdmin(PrivacidadImportExportAdmin):
    list_display = ("usuario",)

    ordering = [
        "usuario__apellidos",
        "usuario__nombres",
    ]

    search_fields = (
        "usuario__apellidos",
        "usuario__nombres",
    )
