from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), # Rota do Admin do Django
    path('', include('projetos.urls')), # Rota para o app de projetos
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
