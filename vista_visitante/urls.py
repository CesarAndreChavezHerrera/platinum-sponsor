from django.urls import path
from .views import visitante

urlpatterns =[
    path('', visitante)
]