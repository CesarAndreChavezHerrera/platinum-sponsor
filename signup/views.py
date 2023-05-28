from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse


# Create your views here.


def signup (request):
    
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        if request.POST['pass1'] == request.POST['pass2']:
            try:
                   user = User.objects.create_user(username=request.POST['last_login'],
                                     password=request.POST['pass1'])
                   user.save()
                   login(request, user)
                   return HttpResponse('Usuario creado correctamente')
                
            except:
                return render (request, 'signup.html',{
                   'form': UserCreationForm,
                   "error": 'El usuario ya existe'
                   
                    
                })
            
        return render (request, 'signup.html',{
                   'form': UserCreationForm,
                   "error": 'Las contaseñas no coinciden'
                    
         })