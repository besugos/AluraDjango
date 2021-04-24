from django.db import models
from datetime import datetime

class Receita(models.Model):
    nome = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo = models.TextField()
    tempo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data = models.DateTimeField(default=datetime.now, blank=True)
