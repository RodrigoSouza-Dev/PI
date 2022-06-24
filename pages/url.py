from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('port', views.port, name='port'),
    path('math', views.math, name='math'),
    path('activ', views.activ, name='activ'),
    path('habil', views.habil, name='habil'),
    path('content', views.content, name='content'),
    path('<int:portugues_id>', views.portugues, name='portugues')
]