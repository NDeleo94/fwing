from django.contrib import admin

from apps.fw.models.email_model import Email

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class EmailResources(resources.ModelResource):
    class Meta:
        model = Email
        fields = "__all__"


# Esta clase hereda de admin.ModelAdmin
class EmailImportExportAdmin(ImportExportModelAdmin):
    resource_classes = [EmailResources]


@admin.register(Email)
class EmailAdmin(EmailImportExportAdmin):
    # list_display = (
    #     "id",
    #     "ciudad",
    #     "estado",
    # )

    # ordering = [
    #     "-estado",
    #     "ciudad",
    #     "id",
    # ]

    list_filter = [
        "estado",
    ]

    # search_fields = ("ciudad",)
