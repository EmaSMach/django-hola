from django.shortcuts import render, redirect
from django.http import HttpResponse
from bienvenido.models import Empleado, Departamento

from bienvenido.forms import EmpleadoForm, DepartamentoForm


def index(request):
    contexto = {
        "saludo":"Hola Mundo",
        "numero":234
    }
    return render(request, "hola.html", contexto)
    #return HttpResponse("Hola Mundo!")

def chau(request):
    return render(request, "chau.html", {})


def empleados(request):
    lista_empleados = Empleado.objects.all()
    contexto = {
        "empleados":lista_empleados,
    }
    return render(request, "empleados.html", contexto)

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

def listar_departamentos(request):
    departamentos = Departamento.objects.all()
    contexto = {
        "departamentos": departamentos,
    }
    return render(request, "lista_departamentos.html", contexto)


def base_template(request):
    return render(request, "base.html", {})

def crear_empleado(request):
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            Empleado = form.save()
            return HttpResponse("EMPLEADO CREADO")

    form = EmpleadoForm()
    contexto = {"form":form,
        "operacion":"CREAR"
    }
    return render(request, "nuevo_empleado.html", contexto)

def editar_empleado(request, id):
    empleado = Empleado.objects.get(pk = id)

    if request.method == "GET":
        form = EmpleadoForm(instance = empleado)
        contexto = {
            "form" : form
        }
        return render(request, "nuevo_empleado.html", contexto)

    elif request.method == "POST":
        form = EmpleadoForm(request.POST, instance = empleado)
        if form.is_valid():
            emp = form.save()
            return redirect("empleado", emp.id)



    

def crear_departamento(request):
    if request.method == "POST":
        form=DepartamentoForm(request.POST)
        if form.is_valid():
            Departamento=form.save()
            return redirect("departamentos_lista")
    form=DepartamentoForm()
    contexto={"form":form}
    return render(request, "nuevo_departamento.html", contexto)