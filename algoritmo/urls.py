from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_algoritmo, name='vista_algoritmo'),
    path('nueva_lista', views.nueva_lista, name='nueva_lista'),
]