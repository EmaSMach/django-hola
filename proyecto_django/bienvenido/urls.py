from django.urls import path
from . import views

urlpatterns = [
    path("hola/", views.index, name="index"),
    path("chau/", views.chau, name="despedida"),
    path("base/", views.base_template),

    path("empleados/", views.empleados),
    path("empleado/<int:id>", views.mostrar_empleado, name="empleado"),
    path("empleado/nuevo/", views.crear_empleado),
    path("empleado/borrar/<int:id>", views.borrar_empleado, name="borrar_empleado"),
    path("empleado/editar/<int:id>", views.editar_empleado, name="editar_empleado"),

    path("departamentos/", views.listar_departamentos, name="departamentos_lista"),
    path("departamento/nuevo/", views.crear_departamento),    

]