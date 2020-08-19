from django.shortcuts import render
from django.http import HttpResponse
from perfiles.models import Usuario,City
# Create your views here.



def formulario(request):
    lista = Usuario.objects.all
    ciudades = City.objects.all
    return render(request, "formulario.html",{"lista":lista,"ciudades":ciudades})

def registro(request):
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
        cedulavalidacion = Usuario.objects.filter(cedula = cedula)
        if cedulavalidacion:
            validacion = 3
            return render(request,"formulario.html",{"validacion":validacion,"ciudades":ciudades,"lista":lista})
        else:
            ciudad = City(id = idciudad)
            usuario = Usuario(nombres = nombre, apellidos = apellidos, cedula = cedula, telefono = telefono, mail = email, ip = "1.0920", ciudad=ciudad)
            usuario.save()
            validacion = 1
            return render(request,"formulario.html",{"validacion":validacion,"ciudades":ciudades,"lista":lista})
    else:
        validacion = 2
        return render(request,"formulario.html",{"validacion":validacion,"apellidos":apellidos,"ciudades":ciudades,"lista":lista})
  