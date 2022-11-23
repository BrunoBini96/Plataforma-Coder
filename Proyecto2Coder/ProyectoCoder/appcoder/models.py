from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()
    def __str__(self):
        return f'{self.nombre} - {self.camada}' 

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    def __str__(self):
        return f'{self.nombre} - {self.apellido} - {self.email}'

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    profesion = models.CharField(max_length = 50)
    def __str__(self):
        return f'{self.nombre} - {self.apellido} - {self.email} - {self.profesion}'


