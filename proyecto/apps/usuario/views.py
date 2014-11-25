from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.models import User
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
			usua.is_active=False
			usua.save()
			#pdb.set_trace()'9ujn9uy'
			#ema=User.objects.get (email=nuevo_ema)
			usuario=Perfil.objects.create(user=usua)
			#usuario=Usuario.objects.create(usuario=ema)
			estado=True
			mensaje=" Usuario registrado correctamente"
			datos={"form":form_re, "mensaje":mensaje , "estado":estado}
			return render_to_response("usuario/registro.html",datos,RequestContext(request))
			
	else:
		form_re=UsuarioForm()
	return render_to_response("usuario/registro.html",{"form":form_re},RequestContext(request))
def login_usuario(request):
	if request.method=="POST":
		form=AuthenticationForm(request.POST)
		if request.session['contador']>2:
			form2=FormCaptcha(request.POST)
			if form2.is_valid():
				pass
			else:
				datos={"form":form,"form2":form2}
				return render_to_response("usuario/login.html",datos,RequestContext(request))
		if(form.is_valid()==False):
			username=request.POST["username"]
			password=request.POST["password"]
			resultado=authenticate(username=username,password=password)
			#pdb.set_trace()
			if resultado is not None:
				if resultado.is_active:
					login(request, resultado)
					del request.session['contador']
					request.session["name"]=username
					return HttpResponseRedirect("/perfil/")
				else:
					login(request, resultado)
					return HttpResponseRedirect("/active/")
			else:
				request.session['contador']=request.session['contador']+1
				aux=request.session['contador']
				estado=True
				mensaje="Error en los datos"+ str(aux)
				if aux>2:
					form2=FormCaptcha()
					datos={"form":form,"form2":form2, "estado":estado, "mensaje":mensaje}
				else:
					datos={"form":form, "estado":estado, "mensaje":mensaje}
				return render_to_response("usuario/login.html",datos,RequestContext(request))
	else:
		request.session['contador']=0		
		form=AuthenticationForm()
	return render_to_response("usuario/login.html",{"form":form},RequestContext(request))
def logout_usuario(request):
	logout(request)
	return HttpResponseRedirect("/login/")
def principal(request):
	return render_to_response("principal.html",{},RequestContext(request))
def perfil_usuario(request):
	#usuario=User.objects.filter(username=)
#	form_per=PerfilForm()
	usuario=request.user
	#if(usuario=="omar"):
	#	estadoo=True
	#	pdb.set_trace()
	#	return render_to_response("usuario/perfil.html",{"estadoo":estadoo},RequestContext(request))
	return render_to_response("usuario/perfil.html",{"usuario":usuario},RequestContext(request))
def modificar_perfil(request):
	if request.user.is_authenticated():
		usu=request.user
		usuario=User.objects.get(username=usu)
		perfil=Perfil.objects.get(user=usuario)
		if request.method=="POST":
			form_per=PerfilForm_modificar(request.POST,request.FILES, instance=perfil)
			if form_per.is_valid():
				form_per.save()
				return HttpResponseRedirect("/perfil/")
		else:
			form_per=PerfilForm_modificar(instance=perfil)
		return render_to_response("usuario/modificar_perfil.html", {"form_per":form_per},RequestContext(request))
	else:
		return HttpResponseRedirect("/login/")
def user_active(request):
	if request.user.is_authenticated():
		usuario=request.user
		if usuario.is_active:
			return HttpResponseRedirect("/perfil/")
		else:
			if request.method=="POST":
				u=User.objects.get(username=usuario)
				perfil=Perfil.objects.get(user=u)
				formulario=PerfilForm(request.POST, request.FILES,instance=perfil)
				if formulario.is_valid():
					formulario.save()
					u.is_active=True
					u.save()
					return HttpResponseRedirect("/perfil/")
			else:
				formulario=PerfilForm()
			return render_to_response("usuario/active.html",{"formulario":formulario},RequestContext(request))
	else:
		return HttpResponseRedirect("/login/")	
#def agregar_tema(request):
#	if (request.method=="POST"):
#		form_tem=TemaForm(request.POST)
#		if(form_tem.is_valid()):
#			tema=request.POST["nombre_tema"]
#			request.session["tema"]=tema
#			form_tem.save()
#			return HttpResponseRedirect("/pregunta/")
#	else:
#		form_tem=TemaForm()
#	return render_to_response("tema/tema.html",{"form_tem":form_tem},RequestContext(request))
#def pregunta(request):
#	#pdb.set_trace()
#	if (request.method=="POST"):
#		form_pre=PreguntaForm(request.POST)
#		tem=Tema.objects.get(nombre_tema=request.session["tema"])
#		if(form_pre.is_valid()):
#			pre=request.POST["pregunta"]
#			request.session["pregunta"]=pre
#			tema=form_pre.save(commit=False)
#			tema.pre=tem
#			tema.save()
#			return HttpResponseRedirect("/respuesta/")
#	else:
#		form_pre=PreguntaForm()
#	return render_to_response("tema/pregunta.html",{"form_pre":form_pre},RequestContext(request))
#def respuesta(request):
#	if (request.method=="POST"):
#		form_res=RespuestaForm(request.POST)
#		pregunta=Pregunta.objects.get(pregunta=request.session["pregunta"])
#		if(form_res.is_valid()):
#			preg=form_res.save(commit=False)
#			preg.res=pregunta
#			preg.save()
#			return HttpResponseRedirect("/respuesta/")
#	else:
#		form_res=RespuestaForm()
#	return render_to_response("tema/respuesta.html",{"form_res":form_res},RequestContext(request))
