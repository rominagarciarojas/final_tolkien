from concurrent.futures.process import _MAX_WINDOWS_WORKERS
from re import S
from django.db import models


# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    promocion = models.IntegerField()
    


class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    cargo = models.CharField(max_length=30, default="")
    titulo_habilitante = models.CharField(max_length=100, default="")


class Materias(models.Model):
    materia = models.CharField(max_length=100)
    curso = models.IntegerField()
    docente = models.CharField(max_length=100)
    modalidad = models.CharField(max_length=100)

class Libro(models.Model):
    autor = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    copia = models.IntegerField()
    editorial = models.CharField(max_length=200)
    nivel = models.CharField(max_length=200)
    retiro = models.CharField(max_length=200)

