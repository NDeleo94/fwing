from django.contrib import admin

from apps.fw.models.carrera_model import Carrera, Titulo, Plan


class TituloInline(admin.TabularInline):
    model = Titulo
    extra = 1


class PlanInline(admin.TabularInline):
    model = Plan
    extra = 1


@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    inlines = [
        TituloInline,
        PlanInline,
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
                    "estado",
                )
            },
        ),
    )
    list_filter = ["estado"]

    search_fields = ("carrera",)


@admin.register(Titulo)
class TituloAdmin(admin.ModelAdmin):
    list_display = ("titulo", "carrera", "estado")
    search_fields = (
        "titulo",
        "carrera__carrera",
    )
    fieldsets = (
        (
            "Datos",
            {
                "fields": (
                    "titulo",
                    "carrera",
                )
            },
        ),
        ("Permisos", {"fields": ("estado",)}),
    )
    list_filter = ["estado"]


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ("plan", "carrera", "estado")
    search_fields = (
        "plan",
        "carrera__carrera",
    )
    fieldsets = (
        (
            "Datos",
            {
                "fields": (
                    "plan",
                    "carrera",
                    "acreditacion",
                    "acreditadora",
                )
            },
        ),
        ("Permisos", {"fields": ("estado",)}),
    )
    list_filter = ["estado"]
