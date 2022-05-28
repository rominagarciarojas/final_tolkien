from alumnos.views import *
from django.urls import path

urlpatterns = [
    path("hola-mundo/", hola_mundo, name="hola-mundo"),
    #path("hola-soy-una-plantilla/", hola_soy_una_plantilla, name="hola-soy-una-plantilla"),
]