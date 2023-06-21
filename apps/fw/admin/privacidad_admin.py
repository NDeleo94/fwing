from django.contrib import admin

from apps.fw.models.privacidad_model import Privacidad


@admin.register(Privacidad)
class PrivacidadAdmin(admin.ModelAdmin):
    list_display = ("usuario",)
