from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso,Profesor,Estudiante,Entregable
from AppCoder.forms import CursoFormulario,ProfesorFormulario,EstudianteFormulario,EntregableFormulario

def inicio(request):
    return render(request, "Appcoder/inicio.html")


def busquedaComision(request):
    return render(request, "AppCoder/busquedaComision.html")

def buscarComision(request):
    if request.GET["comision"]:
        comision= request.GET["comision"]
        cursos = Curso.objects.filter(comision=comision)
        if len(cursos)!=0:
            return render(request, "AppCoder/resultadosBusquedaComision.html", {"cursos":cursos})
        else:
            return render(request, "AppCoder/resultadosBusquedaComision.html", {"mensaje":"No existe la comision ingresada"})
    else:
        return render(request, "AppCoder/resultadosBusquedaComision.html", {"respuesta":"No Ingreso datos"})

def comisionFormulario(request):
    #SI VIENE POR POST
    if request.method=="POST":
        #recibo el formulario valido
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            #guardo su info
            info = miFormulario.cleaned_data
            print(info)
            nombre = info.get("nombre")
            comision = info.get("comision")
            profesor = info.get("profesor")
            curso = Curso(nombre=nombre, comision = comision, profesor = profesor)
            curso.save()
            return render(request, "AppCoder/inicio.html", {"mensaje": "Comision creada"})
        else:
            return render(request, "AppCoder/inicio.html", {"mensaje": "Error"})
    else:
        miFormulario = CursoFormulario()
        return render(request, "AppCoder/comisionFormulario.html", {"miFormulario":miFormulario})


def busquedaProfesor(request):
    return render(request, "Appcoder/busquedaProfesor.html")

def buscarProfe(request):
    if request.GET["nombre"] and request.GET["apellido"]:
        nombre= request.GET["nombre"]
        apellido= request.GET["apellido"]
        #trae muchos, get trae los que cumplen condicion y alt todos sin importar nada
        profesor = Profesor.objects.filter(nombre=nombre,apellido=apellido)
        if len(profesor)!=0:
            return render(request, "AppCoder/resultadosBusquedaProfesor.html", {"profesor":profesor})
        else:
            return render(request, "AppCoder/resultadosBusquedaProfesor.html", {"mensaje":"No existe el profesor ingresado"})
    else:
        return render(request, "AppCoder/resultadosBusquedaProfesor.html", {"respuesta":"No Ingreso datos"})

def profesorFormulario(request):
    
    if request.method == "POST":
        miFormulario = ProfesorFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            profesor = Profesor(nombre=informacion['nombre'],apellido=informacion['apellido'],email=informacion['email'],profesion=informacion['profesion'])

            profesor.save()

            return render(request, "AppCoder/inicio.html", {"mensaje": "Profesor creado"})
        else:
            return render(request, "AppCoder/inicio.html", {"mensaje": "Error"})
    else:
        miFormulario = ProfesorFormulario()
        return render(request, "AppCoder/profesorFormulario.html",{"miFormulario":miFormulario})


def busquedaEstudiante(request):
    return render(request, "Appcoder/busquedaEstudiante.html")

def buscarEstudiante(request):
    if request.GET["nombre"] and request.GET["apellido"]:
        nombre= request.GET["nombre"]
        apellido= request.GET["apellido"]
        estudiante = Estudiante.objects.filter(nombre=nombre,apellido=apellido)
        if len(estudiante)!=0:
            return render(request, "AppCoder/resultadosBusquedaEstudiante.html", {"estudiante":estudiante})
        else:
            return render(request, "AppCoder/resultadosBusquedaEstudiante.html", {"mensaje":"No existe el estudiante ingresado"})
    else:
        return render(request, "AppCoder/resultadosBusquedaEstudiante.html", {"respuesta":"No Ingreso datos"})

def estudianteFormulario(request):

    if request.method == "POST":
        miFormulario = EstudianteFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            estudiante = Estudiante(nombre=informacion['nombre'],apellido=informacion['apellido'],email=informacion['email'])

            estudiante.save()

            return render(request, "AppCoder/inicio.html", {"mensaje": "Estudiante creado"})
        else:
            return render(request, "AppCoder/inicio.html", {"mensaje": "Error"})
    else:
        miFormulario = EstudianteFormulario()
        return render(request, "AppCoder/estudianteFormulario.html",{"miFormulario":miFormulario})


def busquedaEntregables(request):
    return render(request, "Appcoder/busquedaEntregables.html")

def buscarEntregables(request):
    if request.GET["nombre"]:
        nombre= request.GET["nombre"]
        entregable = Entregable.objects.filter(nombre = nombre)
        if len(entregable)!=0:
            return render(request, "AppCoder/resultadosBusquedaEntregable.html", {"entregable":entregable})
        else:
            return render(request, "AppCoder/resultadosBusquedaEntregable.html", {"mensaje":"No existe el entregable ingresado"})
    else:
        return render(request, "AppCoder/resultadosBusquedaEntregable.html", {"respuesta":"No Ingreso datos"})

def entregableFormulario(request):
    #SI VIENE POR POST
    if request.method=="POST":
        #recibo el formulario valido
        miFormulario = EntregableFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            #guardo su info
            info = miFormulario.cleaned_data
            print(info)
            nombre = info.get("nombre")
            fecha_entrega = info.get("fecha_entrega")
            entregado = info.get("entregado")
            entregable = Entregable(nombre=nombre, fecha_entrega = fecha_entrega, entregado = entregado)
            entregable.save()
            return render(request, "AppCoder/inicio.html", {"mensaje": "Entregable creado"})
        else:
            return render(request, "AppCoder/inicio.html", {"mensaje": "Error"})
    else:
        miFormulario = EntregableFormulario()
        return render(request, "AppCoder/entregableFormulario.html", {"miFormulario":miFormulario})
