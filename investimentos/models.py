from django.db import models

# Create your models here.
class Investimento(models.Model):
    nome_investimento = models.CharField('Investimento',max_length=50, null=False, blank=False)
    valor = models.CharField('Valor', max_length=20, null=False, blank=False)
    fonte = models.CharField('Fonte', max_length=50, null=False, blank=False)
    data = models.DateField('Data', null=False, blank=False)
    lucro_mensal = models.CharField('Lucro mensal', max_length=30, null=False, blank=False)
    lucro_anual = models.CharField('Lucro anual', max_length=30, null=False, blank=False)

    def  __str__(self):
        return self.nome_investimeto+" "+self.data