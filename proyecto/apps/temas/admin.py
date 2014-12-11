from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Tema)
admin.site.register(Pregunta)
admin.site.register(Res_correcta)
admin.site.register(Res_incorrecta)
admin.site.register(Sala)