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



def signup (request):
    
    if request.method == 'GET':
        return render(request, 'signup.html')
    if request.method == "POST":
        
        datos_ingresado = request.POST
        if datos_ingresado['pass1'] == datos_ingresado['pass2']:
            try:
                new_user = Usuario.objects.create(
                    name = datos_ingresado['first_name'],
                    last_name = datos_ingresado['last_name'],
                    nickname = datos_ingresado['nickname'],
                    correo = datos_ingresado['email'],
                    password = datos_ingresado['pass1']
                )
                new_user.save
                
                
            
            except:
                return render (request, 'signup.html',{
                   #'form': UserCreationForm,
                   "error": 'El usuario ya existe'
                   
                    
                })
            
        return render (request, 'signup.html',{
                  #'form': UserCreationForm,
                   "error": 'Las contaseñas no coinciden'
                    
         })


# Create your views here.
