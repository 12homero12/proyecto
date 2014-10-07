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

)