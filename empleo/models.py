# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from geoposition.fields import GeopositionField
from datetime import date

# Create your models here.
class Postulante(models.Model):
	ESTADOCIV_CHOICES = (
		(1,"Soltero/a"),
		(2,"Casado/a"),
		(3,"Divorciado/a"),
		(4,"Viudo/a"),
	)
	nombre = models.CharField(max_length=255, verbose_name="Nombre y Apellido")
	domicilio = models.CharField(max_length=500)
	geo = GeopositionField()
	disponibilidad = models.TextField(verbose_name="Disponibilidad Semanal")
	celular = models.CharField(max_length=255, verbose_name="Teléfono Celular", blank=True)
	referencias = models.TextField(verbose_name="Referencias", blank=True)
	dni = models.CharField(max_length=8 ,verbose_name="DNI")
	nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
	hijos = models.IntegerField(verbose_name="Cantidad de hijos", blank=True, null=True)
	estado_civil = models.CharField(max_length=30, verbose_name="Estado Civil", blank=True)
	nacionalidad = models.CharField(max_length=30, verbose_name="Nacionalidad")
	antecedentes = models.TextField(blank=True, verbose_name="Antecedentes")
	observaciones = models.TextField(blank=True, verbose_name="Observaciones")
	foto = models.FileField(upload_to="fotos/", null=True, blank=True, verbose_name="Foto")

	def edad(self):
		today = date.today()
		return today.year - self.nacimiento.year - ((today.month, today.day) < (self.nacimiento.month, self.nacimiento.day))

	def foto_tag(self):
		if self.foto:
			foto = self.foto.url
		else:
			foto = "/static/img/noimg.jpg"
		return u'<img src="%s" />' % (foto)

	def thumb_tag(self):
		if self.foto:
			foto = self.foto.url
		else:
			foto = "/static/img/noimg.jpg"
		return u'<img height="60px" src="%s" />' % (foto)

	foto_tag.short_description = 'Foto'
	foto_tag.allow_tags = True
	thumb_tag.short_description = 'Foto'
	thumb_tag.allow_tags = True

	def __unicode__(self):
		return self.nombre
	
class Puesto(models.Model):
	puesto = models.CharField(max_length=150,verbose_name="Puesto")
	direccion = models.CharField(max_length=250,verbose_name="Dirección")
	direccion_completa = models.CharField(max_length=350,verbose_name="Dirección Completa")
	geo = GeopositionField()
	horario = models.TextField(verbose_name="Horario")
	telefono = models.CharField(max_length=15,verbose_name="Teléfono")
	nombre = models.CharField(max_length=150,verbose_name="Nombre y Apellido")
	observaciones = models.TextField(verbose_name="Observaciones", blank=True, null=True)
	trabajador = models.ForeignKey(Postulante,blank=True,null=True)
