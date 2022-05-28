from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hola_mundo(request):
    return HttpResponse("Hola Mundo")

def hola_soy_una_plantilla(request):
    return HttpResponse(render(request, 'alumnos/index.html', {"nombre":"German"}))