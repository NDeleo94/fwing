from django.contrib import admin

from apps.fw.models.puesto_model import Puesto


@admin.register(Puesto)
class PuestoAdmin(admin.ModelAdmin):
    list_display = (
        "puesto",
        "estado",
    )
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
        ("Permisos", {"fields": ("estado",)}),
    )

    list_filter = [
        "estado",
    ]

    search_fields = ("puesto",)
