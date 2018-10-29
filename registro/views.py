from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona
from django.shortcuts import redirect
# Create your views here.

#importar user
from django.contrib.auth.models import User
#sistema de autenticación 
from django.contrib.auth import authenticate,logout, login as auth_login

from django.contrib.auth.decorators import login_required



def index(request):
    usuario = request.session.get('usuario',None)
    return render(request,'index.html',{'name':'Registro de personas','personas':Persona.objects.all(),'usuario':usuario})

def crear(request):


    run = request.POST.get('run','')
    nombre = request.POST.get('nombre','')
    fecha = request.POST.get('fecha','')
    correo = request.POST.get('correo','')
    telefono = request.POST.get('telefono','')
    region = request.POST.get('region','')
    comuna = request.POST.get('comuna','')
    vivienda = request.POST.get('viviendo','')
    contrasenia = request.POST.get('contrasenia', '')

    persona = Persona(run=run, nombre=nombre, fecha=fecha, correo=correo, telefono=telefono, region=region, comuna=comuna, vivienda=vivienda, contrasenia=contrasenia)
    persona.save()    
    

    return redirect('index')

@login_required(login_url='login')
def eliminar(request,id):
    persona = Persona.objects.get(pk = id)
    persona.delete()
    return redirect('index')

@login_required(login_url='login')
def editar(request):
    nombre = request.POST.get('nombre','')
    correo = request.POST.get('correo','')
    id = request.POST.get('id',0)
    persona = Persona.objects.get(pk = id)
    persona.nombre = nombre
    persona.correo = correo
    persona.save()
    return redirect('index')

def cerrar_session(request):
    del request.session['usuario']
    return redirect('index')

def login(request):
    return render(request,'login.html',{})

def login_iniciar(request):
    correo = request.POST.get('nombre_usuario', '')
    contrasenia = request.POST.get('contrasenia', '')
    persona = Persona.objects.filter(correo=correo).filter(contrasenia=contrasenia)
    print(persona)
    if persona is not None:
        request.session['usuario'] = persona[0].nombre
        request.session['id'] = persona[0].id
        return redirect('index')
    else:
        return HttpResponse('No existe')
    