from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template


def hola (request):
    return HttpResponse("<h1>¡Buenas clase!</h1>")

def fecha (request):
    fecha_actual = datetime.now()
    return HttpResponse(f'La fecha y hora actual es {fecha_actual}')

def calcular_nacimiento(request, edad):
    fecha = datetime.now().year - edad
    return HttpResponse(f'Tu año de nacimiento aproximado para tus {edad} años sería: {fecha}')

def mi_template(request):

    cargar_archivo = open(r'C:\Users\Tomas\OneDrive - CERRO CAPITAN S.R.L\Escritorio\Django clases\django-project\templates\template.html', 'r')
    template = Template(cargar_archivo.read())
    cargar_archivo.close()

    contexto = Context()

    template_renderizado = template.render(contexto)

    return HttpResponse(template_renderizado)