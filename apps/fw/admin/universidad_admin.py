from django.contrib import admin

from apps.fw.models.universidad_model import Universidad


@admin.register(Universidad)
class UniversidadAdmin(admin.ModelAdmin):
    list_display = ("universidad", "estado")
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
        ("Contacto", {"fields": ("email", "telefono")}),
        ("Permisos", {"fields": ("estado",)}),
    )
    list_filter = ["estado"]

    search_fields = (
        "universidad",
        "acronimo",
    )
