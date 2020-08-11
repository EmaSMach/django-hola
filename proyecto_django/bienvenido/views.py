from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hola Mundo!")

def chau(request):
    return HttpResponse("Adiós Mundo!")    