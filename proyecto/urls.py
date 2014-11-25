from django.conf.urls import patterns, include, url
from django.contrib import admin
from django import forms
from proyecto.apps.usuario.views import *
from django.conf import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyecto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include("proyecto.apps.usuario.urls")),
    url(r'^', include("proyecto.apps.temas.urls")),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
    {'document_root':settings.MEDIA_ROOT,}
    ),
)
