from django.shortcuts import render
from django.http import HttpResponse
from bienvenido.models import Empleado

# Create your views here.

def index(request):
    return HttpResponse("Hola Mundo!")

def chau(request):
    return HttpResponse("Adiós Mundo!")

def mostrar_empleado(request, id):
    emp = Empleado.objects.get(pk=id)
    return HttpResponse(emp.nombre)

def borrar_empleado(request, id):
    emp = Empleado.objects.get(pk=id)
    nombre = emp.nombre
    emp.delete()
    return HttpResponse(nombre + " Borrado!")