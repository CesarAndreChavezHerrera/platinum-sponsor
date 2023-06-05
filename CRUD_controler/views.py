from django.http import HttpResponse
from django.shortcuts import render
from CRUD_controler import CRUD_usuario as usuario
# Create your views here.

def prueba(request):
    nombre = "1" 
    datos = None
    tipo_peticion = request.method
    print(tipo_peticion)
    if tipo_peticion == "GET":
        datos = usuario.leer_todo()
        
        pass
    if tipo_peticion == "POST":
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        nick = request.POST.get('nick')
        correo = request.POST.get('correo')
        password = request.POST.get('password')

        usuario.guardar(
            nombre=nombre,
            last_name=apellido,
            nickname=nick,
            correo=correo,
            password=password
            )
        
        pass

    return render(request, 'prueba_datos.html',
                  {"nombre":nombre,"dato":datos}
                  )