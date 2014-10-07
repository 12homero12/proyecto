from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth.models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
import pdb

# Create your views here.

def registro_usuario(request):
	if (request.method=="POST"):
		form_re=UsuarioForm(request.POST)
		if form_re.is_valid():
			#pdb.set_trace()
			nuevo_usua=request.POST["username"]
			#nuevo_ema=request.POST["email"]
			form_re.save()
			usua=User.objects.get (username=nuevo_usua)
			#pdb.set_trace()
			#ema=User.objects.get (email=nuevo_ema)
			usuario=Perfil.objects.create(usuario=usua)
			#usuario=Usuario.objects.create(usuario=ema)
			return HttpResponseRedirect("/perfil/")
	else:
		form_re=UsuarioForm()
	return render_to_response("usuario/registro.html",{"form":form_re},RequestContext(request))
def login_usuario(request):
	if request.method=="POST":
		form=AuthenticationForm(request.POST)
		if(form.is_valid()==False):
			username=request.POST["username"]
			password=request.POST["password"]
			resultado=authenticate(username=username,password=password)
			#pdb.set_trace()
			if resultado:
				login(request, resultado)
				request.session["name"]=username
				return HttpResponseRedirect("/perfil/")
	form=AuthenticationForm()
	return render_to_response("usuario/login.html",{"form":form},RequestContext(request))
def logout_usuario(request):
	logout(request)
	return HttpResponseRedirect("/login/")
def principal(request):
	return render_to_response("principal.html",{},RequestContext(request))
def perfil_usuario(request):
	#usuario=User.objects.filter(username=)
	form_per=PerfilForm()
	return render_to_response("usuario/perfil.html",{"nombre":request.session["name"],"form_per":form_per},RequestContext(request))
