from django.db import models

class Usuario(models.Model):
    nome_usuario = models.CharField(max_lenght=50)
    nome = models.CharField(max_lenght=50)
    senha = models.CharField(max_lenght=50)
    email = models.CharField(max_lenght=70)

class Coffeebreak(models.Model):
    nome = models.CharField(max_lenght=50)
    descricao = models.CharField(max_lenght=300)
    endereco = models.CharField(max_lenght=300)
    latitude = models.DecimalField()
    longitude = models.DecimalField()
    inicio = models.DateTimeField()
    fim = models.DateTimeField()
