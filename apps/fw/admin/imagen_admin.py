from django.contrib import admin

from apps.fw.models.imagen_model import Imagen


@admin.register(Imagen)
class ImagenAdmin(admin.ModelAdmin):
    list_display = (
        "usuario",
        "perfil",
        "estado",
    )

    ordering = [
        "-estado",
        "-perfil",
        "-usuario",
    ]

    search_fields = (
        "usuario__apellidos",
        "usuario__nombres",
    )

    list_filter = [
        "perfil",
        "estado",
    ]
