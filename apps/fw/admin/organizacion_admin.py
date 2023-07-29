from django.contrib import admin

from apps.fw.models.organizacion_model import Organizacion

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class OrganizacionResources(resources.ModelResource):
    class Meta:
        model = Organizacion
        fields = (
            "id",
            "organizacion",
            "tipo",
            "empleados",
            "descripcion",
            "email",
            "web",
            # "estado",
        )


# Esta clase hereda de admin.ModelAdmin
class OrganizacionImportExportAdmin(ImportExportModelAdmin):
    resource_classes = [OrganizacionResources]


@admin.register(Organizacion)
class OrganizacionAdmin(OrganizacionImportExportAdmin):
    list_display = (
        "id",
        "organizacion",
        "tipo",
        "empleados",
        "estado",
    )

    ordering = [
        "-estado",
        "-tipo",
        "-empleados",
        "organizacion",
        "id",
    ]

    fieldsets = (
        (
            "Datos",
            {
                "fields": (
                    "organizacion",
                    "tipo",
                    "empleados",
                    "descripcion",
                )
            },
        ),
        (
            "Contacto",
            {
                "fields": (
                    "email",
                    "web",
                )
            },
        ),
        (
            "Permisos",
            {
                "fields": ("estado",),
            },
        ),
    )

    search_fields = ("organizacion",)

    list_filter = [
        "estado",
        "tipo",
    ]
