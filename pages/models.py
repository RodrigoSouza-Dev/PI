from django.db import models


class Portugues(models.Model):
    titulo = models.CharField(max_length= 200)
    p1 = models.TextField(blank= True)
    p2 = models.TextField(blank= True)
    p3 = models.TextField(blank= True)
    nome_arquivo1 = models.CharField(blank= True, max_length= 200)
    link_arquivo1 = models.URLField(blank= True, max_length= 300)
    nome_arquivo2 = models.CharField(blank= True, max_length= 300)
    id_video = models.TextField(blank= True)
    nome_conteudo =  models.CharField(blank= True, max_length= 300)
    audio_link =  models.TextField(blank= True)
    atividades = models.CharField(blank= True, max_length= 200)
    link_arquivo3 = models.URLField(blank= True, max_length= 300)


class Matematica(models.Model):
    titulo = models.CharField(max_length= 200)
    p1 = models.TextField(blank= True)
    p2 = models.TextField(blank= True)
    p3 = models.TextField(blank= True)
    nome_arquivo1 = models.CharField(blank= True, max_length= 200)
    link_arquivo1 = models.URLField(blank= True, max_length= 300)
    nome_arquivo2 = models.CharField(blank= True, max_length= 300)
    id_video = models.TextField(blank= True)
    atividades = models.CharField(blank= True, max_length= 200)
    link_arquivo3 = models.URLField(blank= True, max_length= 300)

class Habilidades(models.Model):
    titulo = models.CharField(max_length= 200)
    p1 = models.TextField(blank= True)
    p2 = models.TextField(blank= True)
    p3 = models.TextField(blank= True)
   
class Lembrete(models.Model):
    titulo = models.CharField(max_length=200)
    assunto = models.TextField(blank= True)
    p1 = models.TextField(blank= True)
    