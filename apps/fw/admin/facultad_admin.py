from django.contrib import admin

from apps.fw.models.facultad_model import Facultad


@admin.register(Facultad)
class FacultadAdmin(admin.ModelAdmin):
    list_display = ("facultad", "universidad", "estado")
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
        ("Permisos", {"fields": ("estado",)}),
    )
    list_filter = ["estado"]

    search_fields = (
        "facultad",
        "acronimo",
    )
