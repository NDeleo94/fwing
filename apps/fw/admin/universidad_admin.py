from django.contrib import admin

from apps.fw.models.universidad_model import Universidad

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class UniversidadResources(resources.ModelResource):
    class Meta:
        model = Universidad
        fields = (
            "id",
            "universidad",
            "acronimo",
            "domicilio",
            "web",
            "email",
            "telefono",
            # "estado",
        )


# Esta clase hereda de admin.ModelAdmin
class UniversidadImportExportAdmin(ImportExportModelAdmin):
    resource_classes = [UniversidadResources]


@admin.register(Universidad)
class UniversidadAdmin(UniversidadImportExportAdmin):
    list_display = (
        "id",
        "universidad",
        "acronimo",
        "estado",
    )

    ordering = [
        "-estado",
        "acronimo",
        "universidad",
        "id",
    ]

    fieldsets = (
        (
            "Datos",
            {
                "fields": (
                    "universidad",
                    "acronimo",
                    "domicilio",
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
        "universidad",
        "acronimo",
    )
