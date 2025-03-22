from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/<int:id>/', views.portfolio_details, name='portfolio_details'),
]
