from django.shortcuts import render, redirect, get_object_or_404
from itv.models import *
from itv.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def usuarioLogin(request):
    if request.method=='POST':
        formulario=AutenticacionForm(request.POST)
        if formulario.is_valid:
            usuario=request.POST['username']
            clave=request.POST['password']
            acceso=authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request,acceso)
                    return redirect('/')
                else:
                    return render(request, 'errorLogin.html')
            else:
                return render(request, 'errorLogin.html')
    else:
        formulario=AutenticacionForm()
    contexto={'formulario':formulario,
              'navbar': "login"}
    return render(request,'login.html',contexto)


# Funcion para cerrar sesion en la pagina
@login_required(login_url='/login')
def usuarioLogout(request):
    logout(request)
    return redirect('/')

class listarConductor(ListView):
    model = conductor
    template_name = 'listarConductor.html'

class crearConductor(CreateView):
	model = conductor
	fields = ['nombre','vehiculos']
	template_name = 'addConductor.html'
	success_url="/conductores"



class ConductorUpdate(UpdateView):
	model = conductor
	fields = ['nombre','vehiculos']
	template_name = 'updateConductor.html'
	success_url="/"

class DeleteConductor(DeleteView):
	model = conductor
	template_name = 'conductor_confirm_delete.html'
	success_url="/conductores"

def verConductor(request,conductor_id):
	con = conductor.objects.get(pk = conductor_id)
	contexto = {'con':con}
	return render(request,'verConductor.html',contexto)

def verVehiculo(request,vehiculo_id):
	veh = vehiculo.objects.get(pk = vehiculo_id)
	contexto = {'veh':veh}
	return render(request,'verVehiculo.html',contexto)

def editarVehiculo(request,vehiculo_id):
    vehi = get_object_or_404(vehiculo, pk = vehiculo_id)


    if request.method == 'POST':
        formulario = VehiculoForm(request.POST,instance=vehi)
        if formulario.is_valid():
            formulario.save()
            return redirect('/vehiculo/'+ vehiculo_id)
	else:	
	    return render(request,"verVehiculo.html",context)
    else:
        formulario = VehiculoForm(instance=vehi)

    contexto = {'formulario': formulario}

    return render(request, 'editarVehiculo.html', contexto)


	
@staff_member_required
def borrarVehiculo(request,vehiculo_id):
	veh = get_object_or_404(vehiculo, pk = vehiculo_id)
	veh.delete()
	return redirect('/conductores')

def editarConductor(request,conductor_id):
    conn = get_object_or_404(conductor, pk =conductor_id)

    if request.method == 'POST':
        formulario = ConForm(request.POST,instance=conn)
        if formulario.is_valid():
            formulario.save()
            return redirect('/conductores/' + conductor_id)
    else:
        formulario = ConForm(instance=conn)
    contexto = {'formulario': formulario}
    return render(request, 'addVehiculo.html', contexto)
