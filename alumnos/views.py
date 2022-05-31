from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.shortcuts import render
from alumnos.forms import PersonaForm, BuscarPersonasForm, ProfesorForm, BuscarProfesoresForm, BuscarMateriasForm, MateriasForm

from alumnos.models import Persona
from alumnos.models import Profesor
from alumnos.models import Materias

def index(request):
    personas = Persona.objects.all()
    template = loader.get_template('alumnos/index.html')
    context = {
        'personas': personas,
    }
    return HttpResponse(template.render(context, request))

def registroa(request):
    personas = Persona.objects.all()
    template = loader.get_template('alumnos/lista_alumnos.html')
    context = {
        'personas': personas,
    }
    return HttpResponse(template.render(context, request))


def agregar(request):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue cargada con éxito
    '''

    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            promocion = form.cleaned_data['promocion']
            Persona(nombre=nombre, apellido=apellido, email=email, fecha_nacimiento=fecha_nacimiento, promocion=promocion).save()

            return HttpResponseRedirect("/registroa/")
    elif request.method == "GET":
        form = PersonaForm()
    else:
        return HttpResponseBadRequest("Error no conozco ese metodo para esta request")

    
    return render(request, 'alumnos/form_carga.html', {'form': form})


def borrar(request, identificador):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue eliminada con éxito        
    '''
    if request.method == "GET":
        persona = Persona.objects.filter(id=int(identificador)).first()
        if persona:
            persona.delete()
        return HttpResponseRedirect("/registroa/")
    else:
        return HttpResponseBadRequest("Error no conozco ese metodo para esta request")


def actualizar(request, identificador):
    '''
    TODO: implementar una vista para actualización
    '''
    pass


def buscar(request):
    if request.method == "GET":
        form_busqueda = BuscarPersonasForm()
        return render(request, 'alumnos/form_busqueda.html', {"form_busqueda": form_busqueda})

    elif request.method == "POST":
        form_busqueda = BuscarPersonasForm(request.POST)
        if form_busqueda.is_valid():
            palabra_a_buscar = form_busqueda.cleaned_data['palabra_a_buscar']
            personas = Persona.objects.filter(apellido__icontains=palabra_a_buscar)
            

        return  render(request, 'alumnos/lista_alumnos.html', {"personas": personas})


###### HASTA QUE EL REGISTRO DE ALUMNOS ############


def registrop(request):
    profesores = Profesor.objects.all()
    template = loader.get_template('alumnos/lista_profesores.html')
    context = {
        'profesores': profesores,
    }
    return HttpResponse(template.render(context, request))


def agregarp(request):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue cargada con éxito
    '''

    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            cargo = form.cleaned_data['cargo'] 
            titulo_habilitante = form.cleaned_data['titulo_habilitante']
            Profesor(nombre=nombre, apellido=apellido, email=email, fecha_nacimiento=fecha_nacimiento, cargo=cargo, titulo_habilitante=titulo_habilitante).save()

            return HttpResponseRedirect("/registrop/")
    elif request.method == "GET":
        form = ProfesorForm()
    else:
        return HttpResponseBadRequest("Error no conozco ese metodo para esta request")

    
    return render(request, 'alumnos/form_carga_profesores.html', {'form': form})


def borrarp(request, identificador):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue eliminada con éxito        
    '''
    if request.method == "GET":
        profesor = Profesor.objects.filter(id=int(identificador)).first()
        if profesor:
            profesor.delete()
        return HttpResponseRedirect("/registrop/")
    else:
        return HttpResponseBadRequest("Error no conozco ese metodo para esta request")


def actualizarp(request, identificador):
    '''
    TODO: implementar una vista para actualización
    '''
    pass


def buscarp(request):
    if request.method == "GET":
        form_busqueda = BuscarProfesoresForm()
        return render(request, 'alumnos/form_busqueda.html', {"form_busqueda": form_busqueda})

    elif request.method == "POST":
        form_busqueda = BuscarProfesoresForm(request.POST)
        if form_busqueda.is_valid():
            palabra_a_buscar = form_busqueda.cleaned_data['palabra_a_buscar']
            profesores = Profesor.objects.filter(apellido__icontains=palabra_a_buscar)
            
        
        return  render(request, 'alumnos/lista_profesores.html', {"profesores": profesores})
 
 
 
 ###### HASTA QUE EL REGISTRO DE PROFESORES ############


 