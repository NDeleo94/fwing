from django.contrib import admin

from apps.fw.models.imagen_model import Imagen


@admin.register(Imagen)
class ImagenAdmin(admin.ModelAdmin):
    list_display = ("usuario",)
