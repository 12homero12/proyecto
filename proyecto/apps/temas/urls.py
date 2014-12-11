from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'miproyecto.views.home', name='home'),
    url(r'^tema/$', registro_tema),
    url(r'^tema/agregar/(\d+)/$',agregar_pregunta),
    
    url(r'^tema/editar/(\d+)/$',ver_pregunta),
    url(r'^pregunta/editar/(\d+)/$',editar_pregunta),
    url(r'^pregunta/eliminar/(\d+)/$',eliminar_pregunta), 

    url(r'^tema/agregar/respuesta/(\d+)/$',agregar_respuesta),

    url(r'^crearsala/$', crear_sala),
    url(r'^permisos/$',mispermisos),
    url(r'^permisos/agregar/$',agregar_permiso),
    url(r'^espera/$',espera),

)