from django.contrib import admin

from apps.fw.models.carrera_model import Carrera, Titulo


class TituloInline(admin.TabularInline):
    model = Titulo
    extra = 1


@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    inlines = [
        TituloInline,
    ]
    list_display = ("carrera", "facultad", "estado")
    fieldsets = (
        (
            "Datos",
            {
                "fields": (
                    "carrera",
                    "facultad",
                    "web",
                    "plan",
                    "acreditacion",
                    "acreditadora",
                    "estado",
                )
            },
        ),
    )
    list_filter = ["estado"]

    search_fields = ("carrera",)
