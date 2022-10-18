from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
from django.shortcuts import render, redirect
import random
from home.forms import BusquedaHumanoFormulario, HumanoFormulario
from home.models import Humano


def hola (request):
    return HttpResponse('<h1>¡Buenas clase!</h1>')

def fecha (request):
    fecha_actual = datetime.now()
    return HttpResponse(f'La fecha y hora actual es {fecha_actual}')

def calcular_nacimiento(request, edad):
    fecha = datetime.now().year - edad
    return HttpResponse(f'Tu año de nacimiento aproximado para tus {edad} años sería: {fecha}')

def mi_template(request):

    cargar_archivo = open(r'C:\Users\Tomas\OneDrive - CERRO CAPITAN S.R.L\Escritorio\Django clases\django-project\home\templates\mi_template.html', 'r')
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    contexto = Context()
    template_renderizado = template.render(contexto)

    return HttpResponse(template_renderizado)

def tu_template(request, nombre):

    template = loader.get_template('home/tu_template.html')
    template_renderizado = template.render({'persona': nombre})
    
    return HttpResponse(template_renderizado)

def prueba_template(request):

    mi_contexto = {
        'rango': list(range(1,11)),
        'valor_aleatorio': random.randrange(1,11)
    }

    template = loader.get_template('home/prueba_template.html')
    template_renderizado = template.render(mi_contexto)
    
    return HttpResponse(template_renderizado)

def crear_persona(request):

    if request.method == 'POST':
        formulario = HumanoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data['nombre']
            apellido = data['apellido']
            edad = data['edad']
            fecha_creacion = data.get('fecha_creacion', datetime.now())

            persona = Humano(nombre=nombre, apellido=apellido, edad=edad, fecha_creacion=fecha_creacion)
            persona.save()

        return redirect('ver_personas')

    formulario = HumanoFormulario()


    return render(request, 'home/crear_persona.html', {'formulario': formulario})


def ver_personas(request):
    
    formulario = BusquedaHumanoFormulario()

    nombre = request.GET.get('nombre')
    if nombre:
        personas = Humano.objects.filter(nombre__icontains=nombre)
    else:
        personas = Humano.objects.all()


    return render(request, 'home/ver_personas.html', {'personas': personas, 'formulario': formulario})

def index (request):
    return render(request, 'home/index.html')