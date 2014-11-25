from django import forms
from .models import *
from django.forms import ModelForm

class TemaForm(ModelForm):
	class Meta:
		model=Tema

class PreguntaForm(ModelForm):
	class Meta:
		model=Pregunta
		exclude=['tema', 'user']
		
class RespuestasForm(ModelForm):
	class Meta:
		model=Respuesta
		exclude=['pregunta']