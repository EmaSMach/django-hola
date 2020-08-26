from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("chau/", views.chau, name="despedida"),
    path("base/", views.base_template),

    path("empleado/", views.listar_empleados, name="lista_empleados"),
    path("empleado/search/", views.search_empleados),    

    path("empleado/nuevo/", views.crear_empleado),
    path("empleado/<int:id>", views.mostrar_empleado, name="empleado"),
    path("empleado/<int:id>/borrar/", views.borrar_empleado, name="borrar_empleado"),
    path("empleado/<int:id>/editar/", views.editar_empleado, name="editar_empleado"),


    path("departamento/", views.listar_departamentos, name="lista_departamentos"),

    path("departamento/nuevo/", views.crear_departamento),
    path("departamento/<int:id>", views.mostrar_departamento, name="departamento"),
    path("departamento/<int:id>/borrar", views.borrar_departamento, name="borrar_departamento"),

]