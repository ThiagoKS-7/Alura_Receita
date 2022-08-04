from django.db import models

class Pessoa(models.Model) :
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=20)

# Create your models here.
