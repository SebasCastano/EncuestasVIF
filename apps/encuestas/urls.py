from django.urls import path
from apps.encuestas.views import agregar_encuesta_mujer, consultar_encuesta_mujer, agregar_encuesta_hombre, index, \
    consultar_encuesta_hombre

urlpatterns = [
    path('', index, name='index'),
    path('agregar_encuesta_mujer/', agregar_encuesta_mujer, name='agregar_encuesta_mujer'),
    path('consultar_encuesta_mujer/', consultar_encuesta_mujer, name='consultar_encuesta_mujer'),
    path('agregar_encuesta_hombre/', agregar_encuesta_hombre, name='agregar_encuesta_hombre'),
    path('consultar_encuesta_hombre/', consultar_encuesta_hombre, name='consultar_encuesta_hombre')
]