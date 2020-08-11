from django.urls import path
from . import views

urlpatterns = [
    path("hola/", views.index, name="index"),
    path("chau/", views.chau, name="despedida"),
    path("adios/", views.chau, name="despedida"),
    
]