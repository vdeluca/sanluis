# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

class PostulanteAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'edad',"thumb_tag")
	#fields = ( 'foto_tag', )
	readonly_fields = ['foto_tag','edad',]

class AsignacionAdmin(admin.ModelAdmin):
	list_display = ('empleador', 'trabajador', 'fechaInicio', 'fechaFin')

# Register your models here.
admin.site.register(Postulante, PostulanteAdmin)
admin.site.register(Puesto)
admin.site.register(Asignacion, AsignacionAdmin)
