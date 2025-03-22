from django.shortcuts import render
from .models import Projeto

def projeto_list(request):
    projetos = Projeto.objects.all()
    return render(request, 'projetos/projeto_list.html', {'projetos': projetos})
