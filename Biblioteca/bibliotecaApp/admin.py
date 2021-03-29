from django.contrib import admin
from bibliotecaApp import models

admin.site.register(models.Biblioteca)
admin.site.register(models.Autor)
admin.site.register(models.Llibres)
admin.site.register(models.Prestec)
admin.site.register(models.Tematica)