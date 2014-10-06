from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm

class UserForm(UserCreationForm,ModelForm):
	Email=forms.EmailField()