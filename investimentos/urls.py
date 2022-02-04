from django.urls import path
from .views import *

urlpatterns = [
    path('listar', listar_investimentos, name='listar_investimentos'),
    path('cadastrar', cadastrar_investimento, name='cadastrar_investimento'),
    path('listar/<int:id>',listar_investimento_id, name='listar_investimento_id'),
    path('editar/<int:id>',editar_investimento, name='editar_investimento'),
    path('remover/<int:id>',remover_investimento, name='remover_investimento'),
    path('cadastrar_investidor/', cadastrar_investidor, name='cadastrar_investidor'),
    path('logar_investidor/', logar_investidor, name='logar_investidor'),
    path('deslogar_investidor/', deslogar_investidor, name='deslogar_investidor'),
]