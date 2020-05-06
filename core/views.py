from django.shortcuts import render
from django.contrib import messages
from .forms import ContatoForm, ProdutoModelForm
from .models import Produto

# Create your views here.


def contato(request):
    form = ContatoForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            messages.success(request, 'Enviado com sucesso')
            form = ContatoForm
        else:
            messages.error(request, 'Erro ao enviar email')
    context = {'form': form}
    return render(request, 'contato.html', context)


def index(request):
    produtos = Produto.objects.all()
    context = {'produtos': produtos}

    return render(request, 'index.html', context)


def produto(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sucesso!!!')
            form = ProdutoModelForm()
        else:
            messages.error('Algo deu errado :(')
    else:
        form = ProdutoModelForm()
    context = {'form': form}
    return render(request, 'produto.html', context)
