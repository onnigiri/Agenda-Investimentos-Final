from django.shortcuts import redirect, render
from .models import *
from .forms import *

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def listar_investimentos(request):
  investimentos = Investimento.objects.all()
  return render(request, 'investimentos/listar_investimentos.html', {'investimentos' : investimentos})

@login_required()
def cadastrar_investimento(request):
  if request.method == 'POST':
    form = InvestimentoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('listar_investimentos')
  else:
    form = InvestimentoForm()
  return render(request, 'investimentos/form_investimento.html', {'form': form})

def listar_investimento_id(request, id):
  investimento = Investimento.objects.get(id=id)
  return render(request, 'investimentos/lista_investimento.html', {'investimento': investimento})

@login_required()
def editar_investimento(request, id):
  investimento = Investimento.objects.get(id=id)
  form = InvestimentoForm(request.POST or None, instance=investimento)
  if form.is_valid():
    form.save()
    return redirect('listar_investimentos')
  return render(request, 'investimentos/form_investimento.html', {'form': form})

@login_required()
def remover_investimento(request, id):
  investimento = Investimento.objects.get(id=id)
  if request.method == 'POST':
    investimento.delete()
    return redirect('listar_clientes')
  return render(request, 'investimentos/confirma_exclusao.html', {'investimento': investimento}) 


def cadastrar_investidor(request):
  if request.method == 'POST':
    form_investidor = UserCreationForm(request.POST)
    if form_investidor.is_valid():
      form_investidor.save()
      return redirect('listar_investimentos')
  else:
    form_investidor = UserCreationForm()
  return render(request, 'investimentos/form_investidor.html', {'form_investidor': form_investidor})

def logar_investidor(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    investidor = authenticate(request, username=username, password=password)
    if investidor is not None:
      login(request, investidor)
      return redirect('listar_investimentos')
    else:
      messages.error(request, 'As credenciais estão incorretas')
      return redirect('logar_investidor')
  else:
    form_login = AuthenticationForm()
  return render(request, 'investimentos/form_login.html', {'form_login': form_login})


def deslogar_investidor(request):
  logout(request)
  return redirect('logar_investidor')