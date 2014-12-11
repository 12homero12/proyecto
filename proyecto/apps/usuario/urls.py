from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyecto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', principal),
    url(r'^registro/$', registro_usuario),
    url(r'^login/$',login_usuario),
    url(r'^logout/$',logout_usuario),
    url(r'^perfil/$',perfil_usuario),
    url(r'^perfil1/$',perfil1_usuario),
    url(r'^active/$',user_active),
    url(r'^modificar_perfil/$',modificar_perfil),


    
    #url(r'^crear_sala/$',crear_sala),

    #url(r'^tema/$',agregar_tema),
    #url(r'^pregunta/$',pregunta),
    #url(r'^respuesta/$',respuesta),
)