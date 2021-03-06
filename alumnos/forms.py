from logging import PlaceHolder
from django import forms

class PersonaForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    email = forms.EmailField(label="Email")
    # input_format hace que se pueda ingresar la fecha con el formato latino, dia/mes/año
    fecha_nacimiento = forms.DateField(label="fecha_nacimiento", input_formats=["%D/%M/%Y"],
    #widget es para poder agregar un tip para que el usuario sepa como ingresar la fecha
    widget=forms.TextInput(attrs={'placeholder': '30/12/1995'}))
    promocion = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': "2027"}))

class ProfesorForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    email = forms.EmailField(label="Email")
    # input_format hace que se pueda ingresar la fecha con el formato latino, dia/mes/año
    fecha_nacimiento = forms.DateField(label="fecha_nacimiento", input_formats=["%D/%M/%Y"],
    #widget es para poder agregar un tip para que el usuario sepa como ingresar la fecha
    widget=forms.TextInput(attrs={'placeholder': '30/12/1995'}))
    titulo_habilitante = forms.CharField(label="Título habilitante", max_length=100)
    cargo = forms.CharField(label="Cargo", max_length=30)


class MateriasForm(forms.Form):
    materia = forms.CharField(label="Nombre de asignatura", max_length=200)
    curso = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': "1"}))
    docente = forms.CharField(label="Docente a cargo")
    modalidad = forms.CharField(label="Modalidad", max_length=30)


class LibroForm(forms.Form):
    autor = forms.CharField(label="Nombre de autor", max_length=200),
    titulo = forms.CharField(label="Nombre de libro", max_length=200),
    copia = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': "1"})),
    editorial = forms.CharField(label="Nombre de editorial", max_length=200),
    nivel = forms.CharField(label="Nivel: EP / ES", max_length=2),
    retiro = forms.CharField(label="Apellido, Nombre", max_length=200),
    
class BuscarPersonasForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")

class BuscarProfesoresForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")

class BuscarMateriasForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")

class BuscarLibroForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")

class ActualizarPersonaForm(PersonaForm):
    id = forms.IntegerField(widget = forms.HiddenInput())

class ActualizarLibroForm(LibroForm):
    id = forms.IntegerField(widget = forms.HiddenInput())