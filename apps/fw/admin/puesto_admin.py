from django.contrib import admin

from apps.fw.models.puesto_model import Puesto


@admin.register(Puesto)
class PuestoAdmin(admin.ModelAdmin):
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
