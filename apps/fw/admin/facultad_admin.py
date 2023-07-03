from django.contrib import admin

from apps.fw.models.facultad_model import Facultad

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class FacultadResources(resources.ModelResource):
    class Meta:
        model = Facultad
        fields = (
            "id",
            "facultad",
            "acronimo",
            "domicilio",
            "web",
            "email",
            "telefono",
            # "estado",
        )


# Esta clase hereda de admin.ModelAdmin
class FacultadImportExportAdmin(ImportExportModelAdmin):
    resource_classes = [FacultadResources]


@admin.register(Facultad)
class FacultadAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "facultad",
        "universidad",
        "estado",
    )

    ordering = [
        "-estado",
        "-universidad",
        "facultad",
        "id",
    ]

    fieldsets = (
        (
            "Datos",
            {
                "fields": (
                    "facultad",
                    "acronimo",
                    "domicilio",
                    "universidad",
                    "web",
                )
            },
        ),
        (
            "Contacto",
            {
                "fields": (
                    "email",
                    "telefono",
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

    search_fields = (
        "facultad",
        "acronimo",
    )
