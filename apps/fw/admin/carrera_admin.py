from django.contrib import admin

from apps.fw.models.carrera_model import Carrera, Titulo, Plan

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class TituloInline(admin.TabularInline):
    model = Titulo
    extra = 1


class PlanInline(admin.TabularInline):
    model = Plan
    extra = 1


class CarreraResources(resources.ModelResource):
    class Meta:
        model = Carrera
        fields = (
            "id",
            "carrera",
            "web",
            "following",
            "facultad",
            # "estado",
        )


# Esta clase hereda de admin.ModelAdmin
class CarreraImportExportAdmin(ImportExportModelAdmin):
    resource_classes = [CarreraResources]


@admin.register(Carrera)
class CarreraAdmin(CarreraImportExportAdmin):
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


class TituloResources(resources.ModelResource):
    class Meta:
        model = Titulo
        fields = (
            "id",
            "titulo",
            "carrera",
            # "estado",
        )


# Esta clase hereda de admin.ModelAdmin
class TituloImportExportAdmin(ImportExportModelAdmin):
    resource_classes = [TituloResources]


@admin.register(Titulo)
class TituloAdmin(TituloImportExportAdmin):
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


class PlanResources(resources.ModelResource):
    class Meta:
        model = Plan
        fields = (
            "id",
            "plan",
            "acreditacion",
            "acreditadora",
            "carrera",
            # "estado",
        )


# Esta clase hereda de admin.ModelAdmin
class PlanImportExportAdmin(ImportExportModelAdmin):
    resource_classes = [PlanResources]


@admin.register(Plan)
class PlanAdmin(PlanImportExportAdmin):
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
