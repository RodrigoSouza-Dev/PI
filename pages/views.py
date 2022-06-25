from django.shortcuts import render, get_list_or_404, get_object_or_404
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
###################################################################

def math(request):
    
    return render(request, 'math.html')

def activ(request):
    return render(request, 'activ.html')

def habil(request):
    return render(request, 'habil.html')

def content(request):
    return render(request, 'content.html')