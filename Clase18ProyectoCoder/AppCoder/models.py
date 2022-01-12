from django.contrib.auth import forms
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Curso(models.Model):

    nombre = models.CharField(max_length = 40)
    camada = models.IntegerField()

#Para guardar un modelo hay que poner primero python manage.py makemigrations y luego cambiando el make... por solo migrate

class Jugador(models.Model):

    apellido = models.CharField(max_length= 40)
    numero = models.IntegerField()
    esBueno = models.BooleanField()


class PosibleJugador(models.Model):
    
    apellido = models.CharField(max_length=40)
    numero = models.IntegerField()
    edad = models.IntegerField(default= 0)
    equipo = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return f"Apellido: {self.apellido}, Número: {self.numero}"
