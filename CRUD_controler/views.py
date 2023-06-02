from django.http import HttpResponse
from django.shortcuts import render
from CRUD_controler import CRUD_usuario as usuario
# Create your views here.

def prueba(request):
    nombre = "1" 
    tipo_peticion = request.method
    print(tipo_peticion) 
    if tipo_peticion == "GET":
        nombre = request.GET.get('nombre')


        pass
    if tipo_peticion == "POST":

        pass

    return render(request, 'prueba_datos.html',{"nombre":nombre})