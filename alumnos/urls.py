from django.urls import path
from alumnos import views


urlpatterns = [
    path('', views.index, name="index"),
    path('agregar/', views.agregar, name="agregar"),
    path('borrar/<identificador>', views.borrar, name="borrar"),
    path('buscar/', views.buscar, name="buscar"),
]


#urlpatterns = [
#   path("hola-mundo/", hola_mundo, name="hola-mundo"),
#    path("hola-soy-una-plantilla/", hola_soy_una_plantilla, name="hola-soy-una-plantilla"),
#]
