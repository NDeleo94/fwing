from django.contrib import admin

from apps.fw.models.egreso_model import Egreso

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class EgresoResources(resources.ModelResource):
    class Meta:
        model = Egreso
        fields = (
            "id",
            "usuario",
            "carrera",
            "ciclo_egreso",
            "matricula",
            "postgrado",
            # "estado",
        )


# Esta clase hereda de admin.ModelAdmin
class EgresoImportExportAdmin(ImportExportModelAdmin):
    resource_classes = [EgresoResources]


@admin.register(Egreso)
class EgresoAdmin(EgresoImportExportAdmin):
    list_display = (
        "usuario",
        "ciclo_egreso",
        "postgrado",
        "estado",
    )

    ordering = [
        "-estado",
        "-postgrado",
        "ciclo_egreso",
        "usuario",
    ]

    search_fields = (
        "ciclo_egreso",
        "carrera__carrera",
        "usuario__apellidos",
        "usuario__nombres",
    )

    list_filter = [
        "estado",
    ]
