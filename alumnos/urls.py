from django.urls import path
from alumnos import views


urlpatterns = [
    path('', views.index, name="index"),
    path('actualizar/', views.actualizar, name="actualizar_action"),
    path('actualizar/<identificador>', views.actualizar, name="actualizar"),
    path('registroa/', views.registroa, name="registroa"),
    path('registrop/', views.registrop, name="registrop"),
    path('registrom/', views.registrom, name="registrom"),
    path('agregar/', views.agregar, name="agregar"),
    path('agregarp/', views.agregarp, name="agregarp"),
    path('agregarm/', views.agregarm, name="agregarm"),
    path('borrar/<identificador>', views.borrar, name="borrar"),
    path('borrarp/<identificador>', views.borrarp, name="borrarp"),
    path('borrarm/<identificador>', views.borrarm, name="borrarm"),
    path('buscar/', views.buscar, name="buscar"),
    path('buscarp/', views.buscarp, name="buscarp"),
    path('buscarm/', views.buscarm, name="buscarm"),
]

