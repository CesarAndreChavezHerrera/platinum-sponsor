from django.shortcuts import render
from CRUD_controler.models import Usuario 

def login(request):

    if request.method == "POST":
        nickname = request.POST.get("username")
        password = request.POST.get("pass")
        
        datos = None
        try:
            datos = Usuario.objects.get(nickname = nickname)
        except:
            datos = None
            pass
        if datos != None:
            comprobacion = datos.password == password
            print(comprobacion)
            pass
        

        pass

    return render(request, 'login.html')


