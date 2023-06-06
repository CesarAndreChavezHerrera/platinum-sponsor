from django.urls import path
from .views import vista_editor

urlpatterns =[
    path('', vista_editor)
]