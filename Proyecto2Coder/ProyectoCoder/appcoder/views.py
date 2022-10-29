from django.http import HttpResponse
from django.shortcuts import redirect, render
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
    return render(request, "inicio.html")

def lista_curso(request):
    lista = Curso.objects.all()
    
    return render(request, "lista_cursos.html", {"lista_cursos": lista})

def Cursos2(request):
    lista = Curso.objects.all()
    return render(request, "cursos.html", {"lista_cursos" : lista})

def Profesores2(request):
    return render(request,"profesores.html")


def Estudiantes2(request):
    return render(request,"estudiantes.html")

def Entregables2(request):
    return render(request,"entegables.html")

def cursoFormulario(request):
    
    if request.method == 'POST':
         curso = Curso(nombre=request.POST["curso"], camada=request.POST["camada"])
         curso.save()
         return redirect("Cursos")
    else:
        return render(request,"cursoFormulario.html")
    
        




    