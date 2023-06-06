from django.shortcuts import render
from CRUD_controler.models import Usuario 
from django.http import HttpResponse
def login(request):

    if request.method == "POST":
        datos_ingresado = request.POST
        
        try:
            usuarios = Usuario.objects.get(nickname = datos_ingresado['username'])
            pass
        except:

            pass

        pass
    return render(request, 'login.html')


