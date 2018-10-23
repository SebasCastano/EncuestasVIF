from django.urls import path
from apps.encuestas.views import agregar_encuesta_mujer, index

urlpatterns = [
    path('', index, name='index'),
    path('agregar_encuesta_mujer/', agregar_encuesta_mujer, name='agregar_encuesta_mujer'),
]