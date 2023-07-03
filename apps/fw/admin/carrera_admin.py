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

    list_display = (
        "id",
        "carrera",
        "facultad",
        "following",
        "estado",
    )

    ordering = [
        "-estado",
        "-following",
        "facultad",
        "carrera",
        "id",
    ]

    fieldsets = (
        (
            "Datos",
            {
                "fields": (
                    "carrera",
                    "facultad",
                    "web",
                    "following",
                    "estado",
                )
            },
        ),
    )

    list_filter = [
        "following",
        "estado",
    ]

    search_fields = ("carrera",)


@admin.register(Titulo)
class TituloAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "carrera",
        "estado",
    )

    ordering = [
        "-estado",
        "carrera",
        "titulo",
    ]

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


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = (
        "plan",
        "carrera",
        "estado",
    )

    ordering = [
        "-estado",
        "carrera",
        "plan",
    ]

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
