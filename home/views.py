from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
from django.shortcuts import render
import random

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

def crear_persona(request, nombre, apellido):

    persona = Humano(nombre=nombre, apellido=apellido, edad=random.randrange(1,99), fecha_nacimiento=datetime.now())
    persona.save()
    # template = loader.get_template('crear_persona.html')
    # template_renderizado = template.render({'personas': persona, 'nombre': persona.nombre})
    # return HttpResponse(template_renderizado)
    return render(request, 'home/crear_persona.html', {'personas': persona, 'nombre': persona.nombre})


def ver_personas(request):
    
    personas = Humano.objects.all()

    # template = loader.get_template('ver_personas.html')
    # template_renderizado = template.render({'personas': personas})
    # return HttpResponse(template_renderizado)

    return render(request, 'home/ver_personas.html', {'personas': personas})

def index (request):
    return render(request, 'home/index.html')