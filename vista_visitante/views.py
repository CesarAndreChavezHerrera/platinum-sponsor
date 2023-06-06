from django.shortcuts import render

# Create your views here.
def visitante(request):
    return render(request, 'vista_visitante.html')