from django.shortcuts import redirect, render
from avanzado.models import Mascota
from avanzado.forms import MascotaFormulario

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def ver_mascotas(request):

    mascotas = Mascota.objects.all()

    return render(request, 'avanzado/ver_mascotas.html', {'mascotas': mascotas})

def crear_mascota(request):

    formulario = MascotaFormulario()

    if request.method == 'POST':
        formulario = MascotaFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            mascota = Mascota(
                nombre=datos['nombre'], 
                tipo=datos['tipo'], 
                edad=datos['edad'], 
                fecha_nacimiento=datos['fecha_nacimiento']
            )
            mascota.save()
            return redirect('ver_mascotas')

    return render(request, 'avanzado/crear_mascota.html', {'formulario':formulario})

def editar_mascota(request, id):

    mascota = Mascota.objects.get(id=id)
    
    if request.method == 'POST':
        formulario = MascotaFormulario(request.POST)

        if formulario.is_valid():
            datos = formulario.cleaned_data

            mascota.nombre = nombre=datos['nombre']
            mascota.tipo = datos['tipo']
            mascota.edad = datos['edad']
            mascota.fecha_nacimiento = datos['fecha_nacimiento']
            mascota.save()

            return redirect('ver_mascotas')

    formulario = MascotaFormulario(
        initial={
            'nombre': mascota.nombre,
            'tipo': mascota.tipo, 
            'edad': mascota.edad, 
            'fecha_nacimiento': mascota.fecha_nacimiento
        }
    )
    return render(request, 'avanzado/editar_mascota.html', {'formulario':formulario, 'mascota': mascota})

def eliminar_mascota(request, id):

    mascota = Mascota.objects.get(id=id)
    mascota.delete()
    return redirect('ver_mascotas')


class ListaMascotas(ListView): 
    model = Mascota
    template_name= 'avanzado/ver_mascotas_cbv.html'

class CrearMascotas(CreateView):
    model = Mascota
    success_url= '/avanzado/mascotas/'
    template_name= 'avanzado/crear_mascota_cbv.html'
    fields= ['nombre', 'tipo', 'edad', 'fecha_nacimiento']

class EditarMascotas(UpdateView): 
    model = Mascota
    success_url= '/avanzado/mascotas/'
    template_name= 'avanzado/editar_mascota_cbv.html'
    fields= ['nombre', 'tipo', 'edad', 'fecha_nacimiento']


class EliminarMascotas(DeleteView):
    model = Mascota
    success_url= '/avanzado/mascotas/'
    template_name= 'avanzado/eliminar_mascota_cbv.html'
    
# class VerMascotas(): 