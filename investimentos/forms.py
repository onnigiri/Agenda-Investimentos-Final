from django import forms
from .models import *

class InvestimentoForm(forms.ModelForm):
  class Meta:
    model = Investimento
    fields = ['nome_investimento','valor','fonte','data','lucro_mensal','lucro_anual']
    