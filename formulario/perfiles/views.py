from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def formulario(request):
    return render(request, "formulario.html")

def registro(request):
    mensaje="El nombre introducido es: %r" %request.GET["nombre"]
    return HttpResponse(mensaje)