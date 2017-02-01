"""Examen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from itv import views
from itv.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', TemplateView.as_view(template_name='base.html'), name='base'),
	url(r'^login/', views.usuarioLogin, name='Login'),
	url(r'^logout/', views.usuarioLogout, name='Logout'),
	url(r'^conductores/', listarConductor.as_view(), name='Listar Conductores'),
	url(r'^crearConductor/', crearConductor.as_view(), name='Crear Conductor'),
	url(r'^updateConductor/(?P<pk>[\w-]+)$', ConductorUpdate.as_view(), name='Editar Conductor'),
	url(r'^deleteConductor/(?P<pk>[\w-]+)$', DeleteConductor.as_view(), name='Borrar Conductor'),
	url(r'^conductor/(?P<conductor_id>\d+)', views.verConductor, name='Ver Conductor'),
	url(r'^vehiculo/(?P<vehiculo_id>\d+)', views.verVehiculo, name='Ver Vehiculo'),
	url(r'^editarVehiculo/(?P<vehiculo_id>\d+)', views.editarVehiculo, name='Editar Vehiculo'),
	url(r'^borrarVehiculo/(?P<vehiculo_id>\d+)', views.borrarVehiculo, name='Borrar Vehiculo'),
	url(r'^addVehiculo/(?P<conductor_id>\d+)', views.editarConductor, name='add Vehiculo'),
	
]
