
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class centro(models.Model):
	nombre = models.CharField(max_length = 100)

	def __unicode__(self):
		return self.nombre

class vehiculo(models.Model):
	nombre = models.CharField(max_length = 100)
	centro = models.ManyToManyField(centro)
	
	def __unicode__(self):
		return self.nombre

class conductor(models.Model):
	nombre = models.CharField(max_length = 100)
	vehiculos = models.ManyToManyField(vehiculo)
	
	def __unicode__(self):
		return self.nombre

class resultado(models.Model):
	centro = models.ForeignKey(centro, related_name='centro')
	vehiculo = models.ForeignKey(vehiculo, related_name='vehiculo')
	resultado =  models.IntegerField(default=0)

	def __unicode__(self):
		return self.resultado
