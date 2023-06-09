"""
URL configuration for platinum_sponsor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Registro_usuario.views import *
from Home_usuario.views import *
from Proyectos_usuario.views import *
from Perfil_usuario.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('signup/',signup),
    path('inicio/',inicio),
    path('',inicio_visitante),
    path('editor_cap/',editor_capitulo ),
    path('perfil/',perfil),
    
]

