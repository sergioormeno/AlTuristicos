"""AlTuristicos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from apiat import views
from django.http import HttpResponse


urlpatterns = [
    url(r'^$', 'apiat.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^acerca/', 'apiat.views.Acerca', name='Acerca'),
    url(r'^regiones/$', 'apiat.views.Regiones', name='Regiones'),
    url(r'^regiones/(?P<reg_id2>\d{1,2})/$', 'apiat.views.sortr', name='Sort_Regiones'),
    url(r'^provincias/$', 'apiat.views.Provincias', name='Provincias'),
    url(r'^provincias/(?P<prov_id2>\d{1,2})/$', 'apiat.views.sortp', name='Provincias'),
    url(r'^comunas/$', 'apiat.views.Comunas', name='Comunas'),
    url(r'^comunas/(?P<com_id2>\d{1,3})/$', 'apiat.views.sortc', name='Comunas'),
    url(r'^contact/$', 'apiat.views.contact', name='contact'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)