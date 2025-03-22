from django.shortcuts import render
from .models import Projeto

def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

def portfolio(request):
    projetos = Projeto.objects.all()
    return render(request, 'portfolio.html', {'projetos': projetos})

def portfolio_details(request, id):
    projeto = Projeto.objects.get(id=id)
    return render(request, 'portfolio-details.html', {'projeto': projeto})
