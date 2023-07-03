from django.contrib import admin

from apps.fw.models.puesto_model import Puesto

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class PuestoResources(resources.ModelResource):
    class Meta:
        model = Puesto
        fields = (
            "id",
            "puesto",
            "descripcion",
            # "estado",
        )


# Esta clase hereda de admin.ModelAdmin
class PuestoImportExportAdmin(ImportExportModelAdmin):
    resource_classes = [PuestoResources]


@admin.register(Puesto)
class PuestoAdmin(PuestoImportExportAdmin):
    list_display = (
        "id",
        "puesto",
        "estado",
    )

    ordering = [
        "-estado",
        "puesto",
        "id",
    ]

    fieldsets = (
        (
            "Datos",
            {
                "fields": (
                    "puesto",
                    "descripcion",
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

    list_filter = [
        "estado",
    ]

    search_fields = ("puesto",)
