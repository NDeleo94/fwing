from django.contrib import admin

from apps.fw.models.universidad_model import Universidad


@admin.register(Universidad)
class UniversidadAdmin(admin.ModelAdmin):
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
