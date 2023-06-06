from django.urls import path
from.views import signup
from homeview.views import homeview 
urlpatterns = [
    path('',signup ),
    path("home/",homeview)
]

