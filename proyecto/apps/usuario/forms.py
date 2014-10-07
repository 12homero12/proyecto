from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm

class UsuarioForm(UserCreationForm):
	username=forms.CharField(max_length=50, required=True, help_text=False, label="Usuario")
	password2=forms.CharField(help_text=False,widget=forms.PasswordInput, label="Contrasena (confirmar)")
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
		exclude=['usuario']