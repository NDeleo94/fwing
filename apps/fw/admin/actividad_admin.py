from django.contrib import admin

from apps.fw.models.actividad_model import Actividad


@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = (
        "usuario",
        "organizacion",
        "puesto",
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
        "usuario__apellidos",
        "usuario__nombres",
    )
