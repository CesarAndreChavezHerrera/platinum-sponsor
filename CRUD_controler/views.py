from django.http import HttpResponse
from django.shortcuts import render
from CRUD_controler import CRUD_usuario as usuario
# Create your views here.

def prueba(request):
    nombre = "1" 
    datos = None
    id_user = []

    tipo_peticion = request.method
    print(tipo_peticion)
    if tipo_peticion == "GET":
        datos = usuario.leer_todo()
        for a in datos.values():
            print(a["id_user"])

            pass
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
                  {"nombre":nombre,}
                  )