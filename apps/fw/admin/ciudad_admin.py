from django.contrib import admin

from apps.fw.models.ciudad_model import Ciudad

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class CiudadResources(resources.ModelResource):
    class Meta:
        model = Ciudad
        fields = (
            "id",
            "ciudad",
            # "estado",
        )


# Esta clase hereda de admin.ModelAdmin
class CiudadImportExportAdmin(ImportExportModelAdmin):
    resource_classes = [CiudadResources]


@admin.register(Ciudad)
class UniversidadAdmin(CiudadImportExportAdmin):
    list_display = (
        "id",
        "ciudad",
        "estado",
    )

    ordering = [
        "-estado",
        "ciudad",
        "id",
    ]

    list_filter = [
        "estado",
    ]

    search_fields = ("ciudad",)
