from django.contrib import admin

from apps.fw.models.carrera_model import Carrera, Titulo

admin.site.register(Carrera)
admin.site.register(Titulo)
