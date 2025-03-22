from django.urls import path
from . import views

urlpatterns = [
    path('', views.projeto_list, name='projeto_list'),
]
