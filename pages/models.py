from django.db import models
from datetime import datetime

class Portugues(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    imagem = models.ImageField(blank= True)
    data= models.DateTimeField(default= datetime.now, blank= True)
# Create your models here.

class Matematica(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    imagem = models.ImageField(blank= True)
    data= models.DateTimeField(default= datetime.now, blank= True)

class Habilidades(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    imagem = models.ImageField(blank= True)
    data= models.DateTimeField(default= datetime.now, blank= True)

class Lembrete(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    imagem = models.ImageField(blank= True)
    data= models.DateTimeField(default= datetime.now, blank= True)
