from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from CRUD_controler import models
from django.shortcuts import redirect
from django.http import HttpResponse


# Create your views here.


def signup (request):
    
    if request.method == 'GET':
        return render(request, 'signup.html')
    if request.method == "POST":
        
        datos_ingresado = request.POST
        if datos_ingresado['pass1'] == datos_ingresado['pass2']:
            try:
                new_user = models.Usuario.objects.create(
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