from django.urls import path
from alumnos import views


urlpatterns = [
    path('', views.index, name="index"),
    path('registroa/', views.registroa, name="registroa"),
    path('registrop/', views.registrop, name="registrop"),
    path('agregar/', views.agregar, name="agregar"),
    path('agregarp/', views.agregarp, name="agregarp"),
    path('borrar/<identificador>', views.borrar, name="borrar"),
    path('borrarp/<identificador>', views.borrarp, name="borrarp"),
    path('buscar/', views.buscar, name="buscar"),
    path('buscarp/', views.buscarp, name="buscarp"),
]


#urlpatterns = [
#   path("hola-mundo/", hola_mundo, name="hola-mundo"),
#    path("hola-soy-una-plantilla/", hola_soy_una_plantilla, name="hola-soy-una-plantilla"),
#]
