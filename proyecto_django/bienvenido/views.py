from django.shortcuts import render
from django.http import HttpResponse
from bienvenido.models import Empleado

# Create your views here.

def index(request):
    contexto = {
        "saludo":"Hola Mundo",
        "numero":234
    }
    return render(request, "hola.html", contexto)
    #return HttpResponse("Hola Mundo!")

def chau(request):
    return render(request, "chau.html", {})

def mostrar_empleado(request, id):
    emp = Empleado.objects.get(pk=id)
    contexto = {
        "empleado":emp
    }
    return render(request, "empleado.html", contexto)
    #return HttpResponse(emp.nombre)

def borrar_empleado(request, id):
    emp = Empleado.objects.get(pk=id)
    nombre = emp.nombre
    emp.delete()
    return HttpResponse(nombre + " Borrado!")

def empleados(request):
    lista_empleados = Empleado.objects.all()
    contexto = {
        "empleados":lista_empleados,
    }
    return render(request, "empleados.html", contexto)