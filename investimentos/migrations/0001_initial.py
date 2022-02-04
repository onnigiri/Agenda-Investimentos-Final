# Generated by Django 2.2.27 on 2022-02-04 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Investimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_investimento', models.CharField(max_length=50, verbose_name='Investimento')),
                ('valor', models.CharField(max_length=20, verbose_name='Valor')),
                ('fonte', models.CharField(max_length=50, verbose_name='Fonte')),
                ('data', models.DateField(verbose_name='Data')),
                ('lucro_mensal', models.CharField(max_length=30, verbose_name='Lucro mensal')),
                ('lucro_anual', models.CharField(max_length=30, verbose_name='Lucro anual')),
            ],
        ),
    ]
