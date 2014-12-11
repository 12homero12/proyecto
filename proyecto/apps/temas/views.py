from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import *

import pdb

# Create your views here.

def registro_tema(request):
	menu=permisos(request)
	usuario=request.user
	#pdb.set_trace()
	#lista =usuario.user_permissions.all()
	#pdb.set_trace()
	if not usuario.has_perm("usuario.add_tema"):
		estadoo=True
		mensaje="Error no puede acceder a este sitio no tiene permisos"
		datos={"estadoo":estadoo, "mensaje":mensaje,"menu":menu}
		return render_to_response("tema/tema.html",datos, RequestContext(request))
	titulo="Registro de temas"
	tema=Tema.objects.all()
	if request.method=="POST":
		form=TemaForm(request.POST)
		if form.is_valid():
			form.save()
			estado=True
			datos={'titulo':titulo, 'form':form, "estado":estado, "tema":tema,"menu":menu}
			return render_to_response("tema/tema.html", datos, RequestContext(request))
	else:
		form=TemaForm()
	datos={'titulo':titulo, 'form':form, 'tema':tema,"menu":menu}
	return render_to_response("tema/tema.html", datos, RequestContext(request))
def agregar_pregunta(request, id):
	menu=permisos(request)
	usuario=request.user
	#pdb.set_trace()
	if not usuario.has_perm("usuario.add_tema"):
		estadoo=True
		mensaje="Error no puede acceder a este sitio no tiene permisos"
		datos={"estadoo":estadoo, "mensaje":mensaje,"menu":menu}
		return render_to_response("tema/registro_pregunta.html",datos, RequestContext(request))
	pregun=Pregunta.objects.all()
	tema=Tema.objects.get(id=int(id))
	titulo="Registra pregunta para el tema de"+ tema.nombre
	titulo2="Registra la repuesta"
	if request.method=="POST":
		form_pre=PreguntaForm(request.POST)
		form_re=RespuestasCorrectaForm(request.POST)
		if form_pre.is_valid() and form_re.is_valid():
			pregunta=form_pre.save(commit=False)
			usuario=User.objects.get(username=request.user)
			pregunta.tema=tema
			pregunta.user=usuario
			pregunta.save()
			respuesta=form_re.save(commit=False)
			respuesta.pregunta=pregunta
			respuesta.save()
			estado=True
			form_pre=PreguntaForm()
			datos={'titulo':titulo, 'form_pre':form_pre, 'estado':estado, 'titulo2':titulo2, "form_re":form_re, "pregun":pregun,"menu":menu}
			return render_to_response("tema/registro_pregunta.html", datos, RequestContext(request))
	else:
		form_pre=PreguntaForm()
		form_re=RespuestasCorrectaForm()
	datos={'titulo':titulo, 'titulo2':titulo2,'form_pre':form_pre, "form_re":form_re,"pregun":pregun,"menu":menu}
	return render_to_response("tema/registro_pregunta.html", datos, RequestContext(request))
def agregar_respuesta(request, id):
	menu=permisos(request)
	usuario=request.user
	#pdb.set_trace()
	if not usuario.has_perm("usuario.add_tema"):
		estadoo=True
		mensaje="Error no puede acceder a este sitio no tiene permisos"
		datos={"estadoo":estadoo, "mensaje":mensaje,"menu":menu}
		return render_to_response("tema/registro_respuesta.html",datos, RequestContext(request))
	pre=Pregunta.objects.get(id=int(id))
	titulo="Registrar las respuestas incorrectas" + pre.nombre
	if request.method=="POST":
		form_res_in=RespuestasIncorrectaForm(request.POST)
		if form_res_in.is_valid():
			respuesta=form_res_in.save(commit=False)
			respuesta.pregunta=pre
			respuesta.save()
			form_res_in=RespuestasIncorrectaForm()
			estado=True
			datos={'titulo':titulo,'form_res_in':form_res_in,"estado":estado,"menu":menu}
			return render_to_response("tema/registro_respuesta.html", datos, RequestContext(request))
	else:
		form_res_in=RespuestasIncorrectaForm()
	datos={'titulo':titulo,'form_res_in':form_res_in,"menu":menu}
	return render_to_response("tema/registro_respuesta.html", datos, RequestContext(request))

def ver_pregunta(request, id):
	menu=permisos(request)
	usuario=request.user
	#pdb.set_trace()
	if not usuario.has_perm("usuario.add_tema"):
		estadoo=True
		mensaje="Error no puede acceder a este sitio no tiene permisos"
		datos={"estadoo":estadoo, "mensaje":mensaje,"menu":menu}
		return render_to_response("tema/ver_pregunta.html",datos, RequestContext(request))
	tema=Tema.objects.get(id=int(id))
	pregunta=Pregunta.objects.filter(tema=tema)
	datos={'tema':tema, 'pregunta':pregunta,"menu":menu}
	return render_to_response("tema/ver_pregunta.html", datos, RequestContext(request))

def editar_pregunta(request,id):
	menu=permisos(request)
	pregunta=Pregunta.objects.get(id=int(id))
	respuesta=Res_correcta.objects.get(pregunta=pregunta)
	titulo="Editar pregunta"
	titulo2="Editar las respuesta"
	if request.method=="POST":
		form_pre=PreguntaForm(request.POST, instance=pregunta)
		form_re=RespuestasCorrectaForm(request.POST, instance=respuesta)
		if form_pre.is_valid() and form_re.is_valid():
			form_pre.save()
			form_re.save()
			estado=True
			datos={'titulo':titulo, 'form_pre':form_pre, 'estado':estado, 'titulo2':titulo2, "form_re":form_re,"menu":menu}
			return render_to_response("tema/registro_pregunta.html", datos, RequestContext(request))
	else:
		form_pre=PreguntaForm(instance=pregunta)
		form_re=RespuestasCorrectaForm(instance=respuesta)
	datos={'titulo':titulo, 'titulo2':titulo2, 'form_pre':form_pre, "form_re":form_re,"menu":menu}
	return render_to_response("tema/registro_pregunta.html", datos, RequestContext(request))
def eliminar_pregunta(request, id):
	menu=permisos(request)
	pregunta=Pregunta.objects.get(id=int(id))
	id=pregunta.tema.id
	respuestas=Res_correcta.objects.get(pregunta=pregunta)
	pregunta.delete()
	return HttpResponseRedirect("/tema/editar/"+str(id)+"/")
#def agregar_permiso(request):
	#per=listageneral
	#pdb.set_trace()
#	usuario=request.user
#	usuario.permissions.add(per);
#	return HttpResponse("/permisos/editar/")
def crear_sala(request):
	menu=permisos(request)
	if request.user.is_authenticated():
		if request.method=="POST":
			form_sala=SalaForms(request.POST)
			if form_sala.is_valid():
				form_sala.save()
			return HttpResponseRedirect("/espera/")
		else:
			form_sala=SalaForms()
		return render_to_response("tema/crearpartida.html",{"menu":menu,"form_sala":form_sala},RequestContext(request))
	return HttpResponseRedirect("/login/")

def espera(request):
	return render_to_response("usuario/espera.html",{},RequestContext(request))

def  permisos(request):
	listapermisos=[]
	if request.user.has_perm("usuario.add_tema"):
		listapermisos.append({"url":"/tema/","label":"Registro Temas"})
	if request.user.has_perm("usuario.bloques_permisos"):
		listapermisos.append({"url":"/permisosg/","label":"Permisos"})
	return listapermisos
#def mispermisos(request):
#	menu=permisos(request)
#	usuario=request.user
#	#pdb.set_trace()
#	#lista =usuario.user_permissions.all()
#	#pdb.set_trace()
#	if not usuario.has_perm("usuario.add_tema"):
#		estadoo=True
#		mensaje="Error no puede acceder a este sitio no tiene permisos"
#		datos={"estadoo":estadoo, "mensaje":mensaje,"menu":menu}
#		return render_to_response("permisos/permisos.html",datos, RequestContext(request))
#	usuario=User.objects.all()
#	listageneral=[]
#	listageneral.append({"usuario.add_tema"})
#	listageneral.append({"usuario.bloques_permisos"})
#	#pdb.set_trace()
#	return render_to_response("permisos/permisos.html", {"usuario":usuario,"menu":menu}, RequestContext(request))

def permiso(request):
	menu=permisos(request)
	if request.user.is_authenticated():
		if request.method=="POST":
			form_perm=PermisoForm(request.POST)
			if form_perm.is_valid():
				form_perm.save()
			return HttpResponseRedirect("/permisoss/")
		else:
			form_perm=PermisoForm()
		return render_to_response("permisos/permiso.html",{"menu":menu,"form_perm":form_perm},RequestContext(request))
	return HttpResponseRedirect("/login/")
def permisogeneral(request):
	menu=permisos(request)
	if request.user.is_authenticated():
		if request.method=="POST":
			form_permg=PermisosgeFoms(request.POST)
			if form_permg.is_valid():
				nombre=form_permg.save(commit=False)
				#permiso=form_permg.save(commit=False)
				nombre.save()
				#permiso.save()
				name=nombre.user
				if(nombre.permiso.nombre=="add_tema"):
					i=48
				else:
					i=49
				#pdb.set_trace()
				name.user_permissions.add(i)
				estadoo=True
				mensaje="se a registrado permiso con exito"
				dato={"menu":menu,"form_permg":form_permg, "mensaje":mensaje, "estadoo":estadoo}
				return render_to_response("permisos/permisogeneral.html",dato,RequestContext(request))
				
		else:
			form_permg=PermisosgeFoms()
		return render_to_response("permisos/permisogeneral.html",{"menu":menu,"form_permg":form_permg},RequestContext(request))
	return HttpResponseRedirect("/login/")


