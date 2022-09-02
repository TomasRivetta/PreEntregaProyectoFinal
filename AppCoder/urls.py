from django.urls import path
from AppCoder.views import *

urlpatterns = [

    path('', inicio,name='inicio'),

    path('busquedaComision/',busquedaComision, name='busquedaComision'),
    path('buscarComision/',buscarComision, name='buscarComision'),
    path('comisionFormulario/', comisionFormulario,name='comisionFormulario'),

    path('busquedaProfesor/', busquedaProfesor, name='busquedaProfesor'),
    path('buscarProfe/',buscarProfe, name='buscarProfe'),
    path('profesorFormulario/',profesorFormulario, name='profesorFormulario'),

    path('busquedaEstudiante/', busquedaEstudiante, name='busquedaEstudiante'),
    path('buscarEstudiante/', buscarEstudiante, name='buscarEstudiante'),
    path('estudianteFormulario/', estudianteFormulario,name='estudianteFormulario'),

    path('busquedaEntregables/',busquedaEntregables, name='busquedaEntregables'),
    path('buscarEntregables/', buscarEntregables, name='buscarEntregables'),
    path('entregableFormulario/', entregableFormulario,name='entregableFormulario'),


]