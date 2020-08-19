from django.urls import path
from . import views

urlpatterns = [
    path("hola/", views.index, name="index"),
    path("chau/", views.chau, name="despedida"),
    path("empleados/", views.empleados),
    path("detalle/<int:id>", views.mostrar_empleado, name="empleado"),
    path("borrar_emp/<int:id>", views.borrar_empleado),
    path("departamentos/", views.listar_departamentos, name="departamentos_lista"),
]