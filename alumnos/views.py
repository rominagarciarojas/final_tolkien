from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from alumnos.forms import PersonaForm, BuscarPersonasForm, ProfesorForm, BuscarProfesoresForm, BuscarMateriasForm, MateriasForm, ActualizarPersonaForm

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


def actualizar(request, identificador=''):
    '''
    TODO: implementar una vista para actualización
    '''
    if request.method == "GET":
        persona = get_object_or_404(Persona, pk=int(identificador))
        initial = {
            "id": persona.id,
            "nombre": persona.nombre, 
            "apellido": persona.apellido, 
            "email": persona.email,
            "fecha_nacimiento": persona.fecha_nacimiento.strftime("%d/%m/%Y"),
            "promocion": persona.promocion,
        }
    
        form_actualizar = ActualizarPersonaForm(initial=initial)
        return render(request, 'alumnos/form_carga.html', {'form': form_actualizar, 'actualizar': True})
    
    elif request.method == "POST":
        form_actualizar = ActualizarPersonaForm(request.POST)
        if form_actualizar.is_valid():
            persona = get_object_or_404(Persona, pk=form_actualizar.cleaned_data['id'])
            persona.nombre = form_actualizar.cleaned_data['nombre']
            persona.apellido = form_actualizar.cleaned_data['apellido']
            persona.email = form_actualizar.cleaned_data['email']
            persona.fecha_nacimiento = form_actualizar.cleaned_data['fecha_nacimiento']
            persona.promocion = form_actualizar.cleaned_data['promocion']
            persona.save()

            return HttpResponseRedirect(reverse("index"))


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

def registrom(request):
    materias = Materias.objects.all()
    template = loader.get_template('alumnos/lista_materias.html')
    context = {
        'materias': materias,
    }
    return HttpResponse(template.render(context, request))


def agregarm(request):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue cargada con éxito
    '''

    if request.method == "POST":
        form = MateriasForm(request.POST)
        if form.is_valid():

            materia = form.cleaned_data['materia']
            curso = form.cleaned_data['curso']
            docente = form.cleaned_data['docente']
            modalidad = form.cleaned_data['modalidad']
            Materias(materia=materia, curso=curso, docente=docente, modalidad=modalidad).save()

            return HttpResponseRedirect("/registrom/")
    elif request.method == "GET":
        form = MateriasForm()
    else:
        return HttpResponseBadRequest("Error no conozco ese metodo para esta request")

    
    return render(request, 'alumnos/form_carga_materias.html', {'form': form})


def borrarm(request, identificador=''):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue eliminada con éxito        
    '''
    if request.method == "GET":
        materia = Materias.objects.filter(id=int(identificador)).first()
        if materia:
            materia.delete()
        return HttpResponseRedirect("/registrom/")
    else:
        return HttpResponseBadRequest("Error no conozco ese metodo para esta request")


#def actualizarp(request, identificador=''):
    '''
    TODO: implementar una vista para actualización
    '''
    pass


def buscarm(request):
    if request.method == "GET":
        form_busqueda = BuscarMateriasForm()
        return render(request, 'alumnos/form_busqueda.html', {"form_busqueda": form_busqueda})

    elif request.method == "POST":
        form_busqueda = BuscarMateriasForm(request.POST)
        if form_busqueda.is_valid():
            palabra_a_buscar = form_busqueda.cleaned_data['palabra_a_buscar']
            materias = Materias.objects.filter(apellido__icontains=palabra_a_buscar)
            
        
        return  render(request, 'alumnos/lista_materias.html', {"materias": materias})
 
 
 