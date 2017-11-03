# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

class PostulanteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacimiento')


# Register your models here.
admin.site.register(Postulante, PostulanteAdmin)
admin.site.register(Puesto)
