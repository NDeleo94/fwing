from django.contrib import admin

from apps.fw.models.egreso_model import Egreso


@admin.register(Egreso)
class EgresoAdmin(admin.ModelAdmin):
    list_display = ("usuario", "ciclo_egreso", "estado")
    search_fields = (
        "egreso",
        "carrera__carrera",
    )
