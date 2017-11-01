# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from geoposition.fields import GeopositionField

# Create your models here.
class Postulante(models.Model):
	nombre = models.CharField(max_length=255, verbose_name="Nombre y Apellido")
	edad = models.IntegerField(verbose_name="Edad")
	domicilio = models.CharField(max_length=500)
	geo = GeopositionField()
	disponibilidad = models.TextField(verbose_name="Disponibilidad Semanal")
	celular = models.CharField(max_length=255, verbose_name="Teléfono Celular", blank=True)
	referencias = models.TextField(verbose_name="Referencias", blank=True)
	dni = models.CharField(max_length=8 ,verbose_name="DNI")
	nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
	hijos = models.IntegerField(verbose_name="Cantidad de hijos", blank=True)
	estado_civil = models.CharField(max_length=30, verbose_name="Estado Civil", blank=True)
	nacionalidad = models.CharField(max_length=30, verbose_name="Nacionalidad")
	antecedentes = models.TextField(blank=True, verbose_name="Antecedentes")
	observaciones = models.TextField(blank=True, verbose_name="Observaciones")
	
class Puesto(models.Model):
	ESTADOCIV_CHOICES = (
		(1,"Soltero/a"),
		(2,"Casado/a"),
		(3,"Divorciado/a"),
		(4,"Viudo/a"),
	)
	
	puesto = models.CharField(max_length=150,verbose_name="Puesto")
	direccion = models.CharField(max_length=250,verbose_name="Dirección")
	direccion_completa = models.CharField(max_length=350,verbose_name="Dirección Completa")
	geo = GeopositionField()
	horario = models.TextField(verbose_name="Horario")
	telefono = models.CharField(max_length=15,verbose_name="Teléfono")
	nombre = models.CharField(max_length=150,verbose_name="Nombre y Apellido")
	observaciones = models.TextField(verbose_name="Observaciones")
	referencias = models.TextField(verbose_name="Referencias")
