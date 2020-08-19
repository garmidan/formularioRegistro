from django.shortcuts import render
from django.http import HttpResponse
from perfiles.models import Usuario,City
import socket
# Create your views here.

def formulario(request):
    lista = Usuario.objects.all
    ciudades = City.objects.all
    return render(request, "formulario.html",{"lista":lista,"ciudades":ciudades})

#Metodo registro
def registro(request):
    nombre_equipo = socket.gethostname()
    direccion_equipo = socket.gethostbyname(nombre_equipo)
    validacion = 0
    nombre = ""
    nombre= request.GET["nombre"]
    apellidos = request.GET["apellidos"]
    cedula = request.GET["cedula"]
    telefono = request.GET["telefono"]
    email = request.GET["email"]
    idciudad = request.GET["ciudad"]
    if nombre and apellidos and telefono and cedula and email:
        lista = Usuario.objects.all
        ciudades = City.objects.all
        if nombre.isalpha() and apellidos.isalpha():
            try:
                cedulavalidacion = Usuario.objects.filter(cedula = cedula)
                if cedulavalidacion:
                    validacion = 3
                    return render(request,"formulario.html",{"validacion":validacion,"ciudades":ciudades,"lista":lista})
                else:
                    ciudad = City(id = idciudad)
                    usuario = Usuario(nombres = nombre, apellidos = apellidos, cedula = cedula, telefono = telefono, mail = email, ip = direccion_equipo, ciudad=ciudad)
                    usuario.save()
                    validacion = 1
                    return render(request,"formulario.html",{"validacion":validacion,"ciudades":ciudades,"lista":lista})
            except ValueError:
                validacion = 5
                return render(request,"formulario.html",{"validacion":validacion,"ciudades":ciudades,"lista":lista})
        else:
            validacion = 4
            return render(request,"formulario.html",{"validacion":validacion,"ciudades":ciudades,"lista":lista})
    else:
        validacion = 2
        return render(request,"formulario.html",{"validacion":validacion,"apellidos":apellidos,"ciudades":ciudades,"lista":lista})
  