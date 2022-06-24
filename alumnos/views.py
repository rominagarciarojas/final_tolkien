from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from alumnos.forms import PersonaForm, BuscarPersonasForm, ProfesorForm, BuscarProfesoresForm, BuscarMateriasForm, MateriasForm, ActualizarPersonaForm, BuscarLibroForm, ActualizarLibroForm, LibroForm

from alumnos.models import Persona
from alumnos.models import Profesor
from alumnos.models import Materias
from alumnos.models import Libro 

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

    if request.method == "GET":
        persona = Persona.objects.filter(id=int(identificador)).first()
        if persona:
            persona.delete()
        return HttpResponseRedirect("/registroa/")
    else:
        return HttpResponseBadRequest("Error no conozco ese metodo para esta request")


def actualizar(request, identificador=''):

    if request.method == "GET":
        persona = get_object_or_404(Persona, pk=int(identificador))
        initial = {
            "id": persona.id,
            "nombre": persona.nombre, 
            "apellido": persona.apellido, 
            "email": persona.email,
            "fecha_nacimiento": persona.fecha_nacimiento.strftime("%D/%M/%Y"),
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

            return HttpResponseRedirect(reverse("registroa"))


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

    if request.method == "GET":
        profesor = Profesor.objects.filter(id=int(identificador)).first()
        if profesor:
            profesor.delete()
        return HttpResponseRedirect("/registrop/")
    else:
        return HttpResponseBadRequest("Error no conozco ese metodo para esta request")


def actualizarp(request, identificador):

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

    if request.method == "GET":
        materia = Materias.objects.filter(id=int(identificador)).first()
        if materia:
            materia.delete()
        return HttpResponseRedirect("/registrom/")
    else:
        return HttpResponseBadRequest("Error no conozco ese metodo para esta request")


#def actualizarp(request, identificador=''):
  
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
 

 ###### HASTA QUE EL REGISTRO DE MATERIAS ############


def registrol(request):
    libros = Libro.objects.all()
    template = loader.get_template('alumnos/lista_libros.html')
    context = {
        'libros': libros,
    }
    return HttpResponse(template.render(context, request))


def agregarl(request):

    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():

            autor = form.cleaned_data['autor']
            titulo = form.cleaned_data['titulo']
            copia = form.cleaned_data['copia']
            editorial = form.cleaned_data['editorial']
            nivel = form.cleaned_data['nivel']
            retiro = form.cleaned_data['retiro']
            Libro(autor=autor, titulo=titulo, copia=copia, editorial=editorial, nivel=nivel, retiro=retiro).save()

            return HttpResponseRedirect("/registrol/")
    elif request.method == "GET":
        form = LibroForm()
    else:
        return HttpResponseBadRequest("Error no conozco ese metodo para esta request")

    
    return render(request, 'alumnos/form_carga_libros.html', {'form': form})


def borrarl(request, identificador=''):

    if request.method == "GET":
        libro = Libro.objects.filter(id=int(identificador)).first()
        if libro:
            libro.delete()
        return HttpResponseRedirect("/registrol/")
    else:
        return HttpResponseBadRequest("Error no conozco ese metodo para esta request")



def actualizarl(request, identificador=''):

    if request.method == "GET":
        libro = get_object_or_404(Libro, pk=int(identificador))
        initial = {
            "id": libro.id,
            "autor": libro.autor, 
            "titulo": libro.titulo,
            "copia": libro.copia,
            "editorial": libro.editorial,
            "nivel": libro.nivel,
            "retiro": libro.retiro,
        }
    
        form_actualizar_libros = ActualizarLibroForm(initial=initial)
        return render(request, 'alumnos/form_carga_libros.html', {'form': form_actualizar_libros, 'actualizarl': True})
    
    elif request.method == "POST":
        form_actualizar_libros = ActualizarLibroForm(request.POST)
        if form_actualizar_libros.is_valid():
            libro = get_object_or_404(Libro, pk=form_actualizar_libros.cleaned_data['id'])
            libro.autor = form_actualizar_libros.cleaned_data['autor']
            libro.titulo = form_actualizar_libros.cleaned_data['titulo']
            libro.copia = form_actualizar_libros.cleaned_data['copia']
            libro.editorial = form_actualizar_libros.cleaned_data['editorial']
            libro.nivel = form_actualizar_libros.cleaned_data['nivel']
            libro.retiro = form_actualizar_libros.cleaned_data['retiro']
            libro.save()

            return HttpResponseRedirect(reverse("registrol"))


def buscarl(request):
    if request.method == "GET":
        form_busqueda_libros = BuscarLibroForm()
        return render(request, 'alumnos/form_busqueda_libros.html', {"form_busqueda_libros": form_busqueda_libros})

    elif request.method == "POST":
        form_busqueda_libros = BuscarLibroForm(request.POST)
        if form_busqueda_libros.is_valid():
            palabra_a_buscar = form_busqueda_libros.cleaned_data['palabra_a_buscar']
            libros = Libro.objects.filter(titulo__icontains=palabra_a_buscar)
            
        
        return  render(request, 'alumnos/lista_libros.html', {"libros": libros})
 