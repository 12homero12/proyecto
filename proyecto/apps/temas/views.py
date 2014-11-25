from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import *
import pdb

# Create your views here.

def registro_tema(request):
	usuario=request.user
	#pdb.set_trace()
	if not usuario.has_perm("usuario.add_tema"):
		return HttpResponse ("error no tiene permisos")
	titulo="Registro de temas"
	tema=Tema.objects.all()
	if request.method=="POST":
		form=TemaForm(request.POST)
		if form.is_valid():
			form.save()
			estado=True
			datos={'titulo':titulo, 'form':form, "estado":estado, "tema":tema}
			return render_to_response("tema/tema.html", datos, RequestContext(request))
	else:
		form=TemaForm()
	datos={'titulo':titulo, 'form':form, 'tema':tema}
	return render_to_response("tema/tema.html", datos, RequestContext(request))
def agregar_pregunta(request, id):
	tema=Tema.objects.get(id=int(id))
	titulo="Registra pregunta para el tema de"+tema.nombre
	titulo2="Registra las repuestas"
	if request.method=="POST":
		form_pre=PreguntaForm(request.POST)
		form_re=RespuestasForm(request.POST)
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
			datos={'titulo':titulo, 'form_pre':form_pre, 'estado':estado, 'titulo2':titulo2, "form_re":form_re}
			return render_to_response("tema/registro_pregunta.html", datos, RequestContext(request))
	else:
		form_pre=PreguntaForm()
		form_re=RespuestasForm()
	datos={'titulo':titulo, 'titulo2':titulo2,'form_pre':form_pre, "form_re":form_re}
	return render_to_response("tema/registro_pregunta.html", datos, RequestContext(request))

def ver_pregunta(request, id):
	tema=Tema.objects.get(id=int(id))
	pregunta=Pregunta.objects.filter(tema=tema)
	datos={'tema':tema, 'pregunta':pregunta}
	return render_to_response("tema/ver_pregunta.html", datos, RequestContext(request))

def editar_pregunta(request,id):
	pregunta=Pregunta.objects.get(id=int(id))
	respuesta=Respuesta.objects.get(pregunta=pregunta)
	titulo="Editar pregunta"
	titulo2="Editar las respuesta"
	if request.method=="POST":
		form_pre=PreguntaForm(request.POST, instance=pregunta)
		form_re=RespuestasForm(request.POST, instance=respuesta)
		if form_pre.is_valid() and form_re.is_valid():
			form_pre.save()
			form_re.save()
			estado=True
			datos={'titulo':titulo, 'form_pre':form_pre, 'estado':estado, 'titulo2':titulo2, "form_re":form_re}
			return render_to_response("tema/registro_pregunta.html", datos, RequestContext(request))
	else:
		form_pre=PreguntaForm(instance=pregunta)
		form_re=RespuestasForm(instance=respuesta)
	datos={'titulo':titulo, 'titulo2':titulo2, 'form_pre':form_pre, "form_re":form_re}
	return render_to_response("tema/registro_pregunta.html", datos, RequestContext(request))

def eliminar_pregunta(request, id):
	pregunta=Pregunta.objects.get(id=int(id))
	id=pregunta.tema.id
	respuestas=Respuesta.objects.get(pregunta=pregunta)
	pregunta.delete()
	respuesta.dalete()
	return HttpResponseRedirect("/tema/editar/"+str(id)+"/")

