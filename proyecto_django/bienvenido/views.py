from django.shortcuts import render, redirect
from django.http import HttpResponse
from bienvenido.models import Empleado, Departamento

from bienvenido.forms import EmpleadoForm, DepartamentoForm



def index(request):
    contexto = {
        "saludo":"Hola Mundo",
        "numero":234
    }
    return render(request, "bienvenido/hola.html", contexto)
    #return HttpResponse("Hola Mundo!")

def chau(request):
    return render(request, "bienvenido/chau.html", {})


def empleados(request):
    lista_empleados = Empleado.objects.all()
    contexto = {
        "empleados":lista_empleados,
    }
    return render(request, "bienvenido/empleados.html", contexto)


def search_empleados(request):
    print(request.GET)
    nombre = request.GET.get("nombre_empleado", "")

    lista_empleados = Empleado.objects.filter(nombre__icontains = nombre)
    contexto = {
        "empleados":lista_empleados,
        "param_nombre":nombre
    }
    return render(request, "bienvenido/search_empleados.html", contexto)


def mostrar_empleado(request, id):
    emp = Empleado.objects.get(pk=id)
    contexto = {
        "empleado":emp
    }
    return render(request, "bienvenido/empleado.html", contexto)
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
    return render(request, "bienvenido/lista_departamentos.html", contexto)


def base_template(request):
    return render(request, "base.html", {})

def crear_empleado(request):
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            empleado = form.save(commit=False)
            empleado.save()
            return HttpResponse("EMPLEADO CREADO")

    form = EmpleadoForm()
    contexto = {"form":form,
        "operacion":"CREAR"
    }
    return render(request, "bienvenido/nuevo_empleado.html", contexto)

def editar_empleado(request, id):
    empleado = Empleado.objects.get(pk = id)

    if request.method == "GET":
        form = EmpleadoForm(instance = empleado)
        contexto = {
            "form" : form
        }
        return render(request, "bienvenido/nuevo_empleado.html", contexto)

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