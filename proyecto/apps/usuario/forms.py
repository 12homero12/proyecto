#encoding:utf-8
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm


from captcha.fields import ReCaptchaField
#from django.contrib.auth.forms.models import User

class FormCaptcha(forms.Form):
        captcha = ReCaptchaField(attrs={'theme':'clean'})

class UsuarioForm(UserCreationForm):
	username=forms.CharField(max_length=50, required=True, help_text=False, label="Usuario")
	password2=forms.CharField(help_text=False, widget=forms.PasswordInput, label="Contrasena (confirmar)")
	email=forms.EmailField(max_length=100, required=True, label="Email")
	class Meta:
		model=User
		fields=("username","password1","password2","email")
	def save(self, commit=True):
		user=super(UsuarioForm, self).save(commit=False)
		user.email=self.cleaned_data.get("email")
		if commit:
			user.save()
		return user
class PerfilForm(ModelForm):
	class Meta:
		model=Perfil
		exclude=['user']
class PerfilForm_modificar(ModelForm):
	class Meta:
		model=Perfil
		exclude=['user']
#class TemaForm(ModelForm):
#	class Meta:
#		model=Tema
#class PreguntaForm(ModelForm):
#	class Meta:
#		model=Pregunta
#		exclude=['pre']
#class RespuestaForm(ModelForm):
#	class Meta:
#		model=Respuesta
#		exclude=['res']
