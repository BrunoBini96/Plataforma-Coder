from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso
from  django.http import HttpResponse
# Create your views here.

def curso1(request,nombre1,camada1):
    curso = Curso(nombre=nombre1, camada=camada1)
    curso.save()
    return HttpResponse (f"""
                         <p> Curso: {curso.nombre} - Camada: {curso.camada} agregado! </p>
                         """)

def inicio (request):
    return HttpResponse("Vista inicio")

def lista_curso(request):
    lista = Curso.objects.all()
    
    return render(request, "lista_cursos.html", {"lista_cursos": lista})

def Cursos2(request):
    return HttpResponse("Vista cursos")

def Profesores2(request):
    return HttpResponse("Vista Profesores")


def Estudiantes2(request):
    return HttpResponse("Vista Estudiantes")



def Entregables2(request):
    return HttpResponse("Vista Entregables")





    