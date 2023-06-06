from django.shortcuts import render
from CRUD_controler.models import Usuario 
from django.http import HttpResponse


def login(request):
    if request.method == "GET":
        return render(request, 'login.html',{'error_mensaje':" "})
        pass

    if request.method == "POST":
        datos_ingresado = request.POST

        if datos_ingresado['nickname'] == "":
            return render(
                request, 
                'login.html',
                {'error_mensaje':"Nombre de usuario vacio"}
                )
            pass

        if datos_ingresado['pass'] == "":
            return render(
                request, 
                'login.html',
                {'error_mensaje':"contraseña esta vacio"}
                )
            pass

        try:
            leer_usuario = Usuario.objects.get(nickname = datos_ingresado['nickname'])
            
            if leer_usuario.password == datos_ingresado['pass']:
                print("hola")
                return HttpResponse("Redirigir a homeview")
                pass
            else:
                return render(request, 'login.html',{'error_mensaje':"error en la contraseña"})
                pass
            pass
        except:

            pass
        return render(request, 'login.html',{'error_mensaje':" "})
        pass



