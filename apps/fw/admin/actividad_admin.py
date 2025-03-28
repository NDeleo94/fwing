from django.contrib import admin

from apps.fw.models.actividad_model import Actividad

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ActividadResources(resources.ModelResource):
    class Meta:
        model = Actividad
        fields = (
            "id",
            "usuario",
            "organizacion",
            "ciudad",
            "puesto",
            "modalidad",
            "seniority",
            "inicio",
            "fin",
            # "estado",
        )


# Esta clase hereda de admin.ModelAdmin
class ActividadImportExportAdmin(ImportExportModelAdmin):
    resource_classes = [ActividadResources]


@admin.register(Actividad)
class ActividadAdmin(ActividadImportExportAdmin):
    list_display = (
        "usuario",
        "organizacion",
        "puesto",
        "modalidad",
        "seniority",
        "estado",
    )

    ordering = [
        "-estado",
        "organizacion",
        "puesto",
        "usuario",
    ]

    list_filter = [
        "estado",
    ]

    search_fields = (
        "organizacion__organizacion",
        "puesto__puesto",
        "ciudad__ciudad",
        "usuario__apellidos",
        "usuario__nombres",
    )
