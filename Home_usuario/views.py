from django.shortcuts import render

def inicio(request):

    return render(request, "home.html")
    pass

def inicio_visitante(request):
    return render(request,"vista_visitante.html")

# Create your views here.
