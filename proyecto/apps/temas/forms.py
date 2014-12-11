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
		
class RespuestasCorrectaForm(ModelForm):
	class Meta:
		model=Res_correcta
		exclude=['pregunta']
		
class RespuestasIncorrectaForm(ModelForm):
	class  Meta:
		model=Res_incorrecta
		exclude=['pregunta']
class SalaForms(ModelForm):
	tema=forms.ModelMultipleChoiceField(queryset=Tema.objects.all(), widget=forms.CheckboxSelectMultiple(), required=True)
	class Meta:
		model=Sala
		exclude=["usuario"]
class PermisoForm(ModelForm):
	class Meta:
		model=permiso
class PermisosgeFoms(ModelForm):
	class Meta:
		model=permisogeneral