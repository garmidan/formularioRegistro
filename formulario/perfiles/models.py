from django.db import models

class City(models.Model):
    nombre = models.CharField()

class Users(models.Model):
    nombres = models.CharField()
    apellidos = models.CharField()
    cedula = models.IntegerField()
    telefono = models.CharField(max_length=10)
    mail = models.EmailField()
    ip = models.CharField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

