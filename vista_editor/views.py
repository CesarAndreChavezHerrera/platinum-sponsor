from django.shortcuts import render

# Create your views here.
def vista_editor(request):
    return render(request, 'editor_cap.html')