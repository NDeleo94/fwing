from django.contrib import admin

from apps.fw.models.log_siu_model import LogSIU

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class LogSIUResources(resources.ModelResource):
    class Meta:
        model = LogSIU
        fields = (
            "id",
            "cantidad",
            "origen",
            "fecha",
        )


# Esta clase hereda de admin.ModelAdmin
class LogSIUImportExportAdmin(ImportExportModelAdmin):
    resource_classes = [LogSIUResources]


@admin.register(LogSIU)
class LogSIUAdmin(LogSIUImportExportAdmin):
    list_display = (
        "id",
        "cantidad",
        "origen",
        "fecha",
    )

    ordering = [
        "fecha",
        "origen",
        "cantidad",
        "id",
    ]

    search_fields = ("fecha",)

    def has_add_permission(self, request):
        # Disable the "Add" button in the admin
        return False
