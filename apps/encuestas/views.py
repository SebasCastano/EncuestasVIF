from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.
from apps.encuestas.forms import AgregarEncuestaMujerForm, AgregarEncuestaHombreForm
from apps.encuestas.models import DatosMujeres, DatosHombres


@login_required
def index(request):
    return render(request, 'encuesta/index.html')

@login_required
def agregar_encuesta_mujer (request):
    form = AgregarEncuestaMujerForm()
    if request.method == 'POST':
        form = AgregarEncuestaMujerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Encuesta registrada exitosamente')
            return redirect(agregar_encuesta_mujer)
        else:
            print(form.errors)
            messages.error(request, 'No se pudo registrar la encuesta')
    contexto = {'form': form}
    return render(request, 'encuesta/agregar_encuesta_mujer.html', contexto)

@login_required
def agregar_encuesta_hombre(request):
    form = AgregarEncuestaHombreForm()
    if request.method == 'POST':
        form = AgregarEncuestaHombreForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Encuesta registrada exitosamente')
            return redirect(agregar_encuesta_hombre)
        else:
            print(form.errors)
            messages.error(request, 'No se pudo registrar la encuesta')
    contexto = {'form': form}
    return render(request, 'encuesta/agregar_encuesta_hombre.html', contexto)

@login_required
def consultar_encuesta_mujer(request):
    datos = list(DatosMujeres.objects.all())
    contador = 1
    contexto = {'datos': datos, 'contador': contador}
    return render(request, 'encuesta/consultar_encuesta_mujer.html', contexto)

@login_required
def consultar_encuesta_hombre(request):
    datos = list(DatosHombres.objects.all())
    contador = 1
    contexto = {'datos': datos, 'contador': contador}
    return render(request, 'encuesta/consultar_encuesta_hombre.html', contexto)