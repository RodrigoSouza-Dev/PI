from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import FileResponse, Http404, HttpResponse
import re, os
import os
from django.views.decorators.csrf import csrf_exempt
from .models import Portugues, Matematica, Habilidades, Lembrete

def index(request):
    return render(request, 'index.html')
# Create your views here.



def port(request):
    portugues = Portugues.objects.all( )

    dados= {
        'portugues':portugues
    }
    return render(request, 'port.html', dados)

def portugues(request, portugues_id):
    portugues = get_object_or_404(Portugues, pk=portugues_id)

    port_a_exibir = {
        'portugues': portugues
    }

    return render(request, 'portugues.html', port_a_exibir) 





def math(request):
    matematica = Matematica.objects.all( )

    dados= {
        'matematica':matematica
    }

    return render(request, 'math.html', dados)

def matematica(request, matematica_id):
    matematica = get_object_or_404(Matematica, pk=matematica_id)

    math_a_exibir = {
        'matematica': matematica
    }

    return render(request, 'matematica.html', math_a_exibir) 
#####################################################################
def habil(request):
    habilidades = Habilidades.objects.all( )

    dados= {
        'habilidades': habilidades
    }

    return render(request, 'habil.html', dados)

def habilidades(request, habilidades_id):
    habilidades = get_object_or_404(Habilidades, pk=habilidades_id)

    habil_a_exibir = {
        'habilidades': habilidade
    }

    return render(request, 'habilidades.html', habil_a_exibir) 

############################################
