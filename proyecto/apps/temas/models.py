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
class permiso(models.Model):
	nombre=models.CharField(max_length=100)
	class Meta:
		permissions=(
			("add_tema","add_tema"),
			("bloques_permisos","bloques_permisos"),
		)
	def __unicode__(self):
		return self.nombre
class permisogeneral(models.Model):
	user=models.ForeignKey(User)
	permiso=models.ForeignKey(permiso)

#class Respuesta(models.Model):
#	repuesta_correcta=models.CharField(max_length=500)
#	respuesta=models.CharField(max_length=500)
#	pregunta=models.ForeignKey(Pregunta)
#	def __unicode__(self):
#		return self.pregunta
class Res_correcta(models.Model):
	respuesta_correcta=models.CharField(max_length=500)
	pregunta=models.ForeignKey(Pregunta)
#	def __unicode__(self):
#		return self.pregunta
class Res_incorrecta(models.Model):
	respuesta_incorrecta=models.CharField(max_length=500)
	pregunta=models.ForeignKey(Pregunta)
	#def __unicode__(self):
	#	return self.pregunta
class Sala(models.Model):
	usuario=models.ForeignKey(User)
	nombre=models.CharField(max_length=100)
	cantidad=models.IntegerField()
	tema=models.ManyToManyField(Tema,blank=True)
