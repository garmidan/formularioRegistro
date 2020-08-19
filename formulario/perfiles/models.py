from django.db import models

class City(models.Model):
    nombre = models.CharField(max_length=30)

class Usuario(models.Model):
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=40)
    cedula = models.IntegerField()
    telefono = models.CharField(max_length=10)
    mail = models.EmailField()
    ip = models.CharField(max_length=30)
    ciudad = models.ForeignKey(City, on_delete=models.CASCADE)

