from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField(max_length=10)

class Profesor(models.Model):
    nombre= models.CharField(max_length=50)
    legajo = models.IntegerField(max_length=10)

class Institucion(models.Model):
    ciudad = models.CharField(max_length=50)
    telefono = models.IntegerField(max_length=20)