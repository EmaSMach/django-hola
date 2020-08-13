from django.urls import path
from . import views

urlpatterns = [
    path("hola/", views.index, name="index"),
    path("chau/", views.chau, name="despedida"),
    path("empleado/<int:id>", views.mostrar_empleado, name="empleado"),
    path("borrar_emp/<int:id>", views.borrar_empleado),
 
]