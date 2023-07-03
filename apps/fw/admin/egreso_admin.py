from django.contrib import admin

from apps.fw.models.egreso_model import Egreso


@admin.register(Egreso)
class EgresoAdmin(admin.ModelAdmin):
    list_display = (
        "usuario",
        "ciclo_egreso",
        "estado",
    )

    ordering = [
        "-estado",
        "ciclo_egreso",
        "usuario",
    ]

    search_fields = (
        "ciclo_egreso",
        "carrera__carrera",
        "usuario__apellidos",
        "usuario__nombres",
    )

    list_filter = [
        "estado",
    ]
