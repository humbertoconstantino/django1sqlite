from django.shortcuts import render
from .models import Produto

# Create your views here.
def index(request):
    produtos = Produto.objects.all()
    context = {
        'curso': 'Programação WEB com Django Framework',
        'produtos': produtos
    }
    return render(request,'index.html', context)

def contato(request):
    return render(request,'contato.html')

def produto(request, pk):
    if str(request.user) == 'humberto':
        teste = 'Admin'
    else:
        teste = 'Usuário comum'
        print(pk)
    prod = Produto.objects.get(id=pk)
    context = {
        'nome': teste,
        'produto': prod
    }
    return render(request,'produto.html', context)