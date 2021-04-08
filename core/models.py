from django.db import models

# Create your models here.

class Produto(models.Model):

    nome = models.CharField('nome', max_length=100)
    preco = models.DecimalField('preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque')

    # Apresentando o  objeto de acordo com o que a gente quer
    def __str__(self):
        return f'{self.nome}'

class Cliente(models.Model):

    nome = models.CharField('nome', max_length=100)
    sobrenome = models.CharField('sobrenome', max_length=100)
    email = models.EmailField('Email',max_length=100)

    # Apresentando o  objeto de acordo com o que a gente quer
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'