from django.db import models
from django.contrib.auth.models import User
from .thumbs import ImageWithThumbsField
# Create your models here.

#class Usuario(models.Model):
#	usuario= models.OneToOneField(User)
#	Email= models.EmailField(User)
	#def __unicode__(self):
	#	return(self.)
class Perfil(models.Model):
	usuario=models.ManyToManyField(User)
	avatar = ImageWithThumbsField(upload_to="img_user", sizes=(50,50))
class Tema(models.Model):
	nombre_tema=models.CharField(max_length=100, unique=True , null=True)
	def __unicode__(self):
		return (self.nombre_tema)
