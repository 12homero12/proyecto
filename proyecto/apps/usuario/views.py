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
			#usuario=Perfil.objects.create(usuario=usua)
			#usuario=Usuario.objects.create(usuario=ema)
			return HttpResponseRedirect("/login/")
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
def agregar_tema(request):
	if (request.method=="POST"):
		form_tem=TemaForm(request.POST)
		if(form_tem.is_valid()):
			tema=request.POST["nombre_tema"]
			request.session["tema"]=tema
			form_tem.save()
			return HttpResponseRedirect("/pregunta/")
	else:
		form_tem=TemaForm()
	return render_to_response("tema/tema.html",{"form_tem":form_tem},RequestContext(request))
def pregunta(request):
	#pdb.set_trace()
	if (request.method=="POST"):
		form_pre=PreguntaForm(request.POST)
		tem=Tema.objects.get(nombre_tema=request.session["tema"])
		if(form_pre.is_valid()):
			pre=request.POST["pregunta"]
			request.session["pregunta"]=pre
			tema=form_pre.save(commit=False)
			tema.pre=tem
			tema.save()
			return HttpResponseRedirect("/respuesta/")
	else:
		form_pre=PreguntaForm()
	return render_to_response("tema/pregunta.html",{"form_pre":form_pre},RequestContext(request))
def respuesta(request):
	if (request.method=="POST"):
		form_res=RespuestaForm(request.POST)
		pregunta=Pregunta.objects.get(pregunta=request.session["pregunta"])
		if(form_res.is_valid()):
			preg=form_res.save(commit=False)
			preg.res=pregunta
			preg.save()
			return HttpResponseRedirect("/respuesta/")
	else:
		form_res=RespuestaForm()
	return render_to_response("tema/respuesta.html",{"form_res":form_res},RequestContext(request))
