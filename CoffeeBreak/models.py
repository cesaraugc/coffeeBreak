from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome_usuario = models.CharField(max_length=50)
    nome = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)
    email = models.CharField(max_length=70)

class Coffeebreak(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=300)
    endereco = models.CharField(max_length=300)
    latitude = models.DecimalField(decimal_places=13, max_digits=15)
    longitude = models.DecimalField(decimal_places=13, max_digits=15)
    inicio = models.DateTimeField()
    fim = models.DateTimeField()
