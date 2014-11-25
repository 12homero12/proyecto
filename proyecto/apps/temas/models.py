from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tema(models.Model):
	nombre= models.CharField(max_length=50, unique=True)
	def __unicode__(self):
		return self.nombre
	
class Pregunta(models.Model):
	user=models.ForeignKey(User)
	nombre=models.CharField(max_length=500)
	tema=models.ForeignKey(Tema)
	def __unicode__(self):
		return self.nombre

class Respuesta(models.Model):
	repuesta_correcta=models.CharField(max_length=500)
	respuesta=models.CharField(max_length=500)
	pregunta=models.ForeignKey(Pregunta)
	#def __unicode__(self):
	#	return self.pregunta
	def __str__(self):
		return self.pregunta
