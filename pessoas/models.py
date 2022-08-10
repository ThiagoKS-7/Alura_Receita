from django.db import models

class Pessoa(models.Model) :
    nome_pessoa = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome_pessoa;
