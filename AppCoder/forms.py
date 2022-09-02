#CREACION DE OFRMUILARIO CON DJANGO
from django import forms

class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    comision = forms.IntegerField()
    profesor = forms.CharField(max_length=50)

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=50)
    
class EstudianteFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()

class EntregableFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    fecha_entrega = forms.CharField(max_length=50)
    entregado = forms.CharField(max_length=50)