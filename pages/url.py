from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('port', views.port, name='port'),
    path('math', views.math, name='math'),
    path('habil', views.habil, name='habil'),
    path('<int:portugues_id>', views.portugues, name='portugues'),
    path('<int:matematica_id>', views.matematica, name='matematica'),
    path('<int:habilidades_id>', views.habilidades, name='habilidades'),
]