from django.contrib import admin

from apps.fw.models.organizacion_model import Organizacion


@admin.register(Organizacion)
class OrganizacionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "organizacion",
        "tipo",
        "estado",
    )

    ordering = [
        "-estado",
        "-tipo",
        "organizacion",
        "id",
    ]

    fieldsets = (
        (
            "Datos",
            {
                "fields": (
                    "organizacion",
                    "tipo",
                    "descripcion",
                )
            },
        ),
        (
            "Contacto",
            {
                "fields": (
                    "email",
                    "web",
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

    search_fields = ("organizacion",)

    list_filter = [
        "estado",
        "tipo",
    ]
