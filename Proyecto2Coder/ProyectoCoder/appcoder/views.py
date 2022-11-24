from .forms import CursoFormulario, ProfesorFormulario
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Curso, Profesor
from  django.http import HttpResponse
from django.views.generic import ListView,DeleteView,CreateView,UpdateView,DetailView
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
        
        mi_formulario = CursoFormulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            curso = Curso(nombre=data['curso'], camada=data['camada'])
            curso.save()
            return redirect('Cursos')
    else:
        mi_formulario = CursoFormulario()
    return render(request,"cursoFormulario.html", {'mi_formulario': mi_formulario})

def busqueda_camada(request):
    return render(request,'busqueda_camada.html')      


def buscar(request):
    camada_buscada = request.GET['camada']
    
    curso =  Curso.objects.get(camada = camada_buscada)
    
    return render(request, 'resultadoBusqueda.html', {'curso' : curso, 'camada' : camada_buscada})
    

def listaCursos(request):
    
    cursos = Curso.objects.all()
    return render(request, "leerCursos.html",{"cursos": cursos})


def listaProfesores(request):
    profesores = Profesor.objects.all
    return render(request, 'leerProfesores.html', {'profesores': profesores} )
    

def crea_profesor(request):
    if request.method == 'POST':
        
        mi_formulario = ProfesorFormulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            profesor = Profesor(nombre=data['nombre'], apellido=data['apellido'],email=data['email'],profesion=data['profesion'])
            profesor.save()
            return redirect('ListaProfesores')
    else:
        mi_formulario = ProfesorFormulario()
    return render(request,"profesorFormulario.html", {'mi_formulario': mi_formulario})

def eliminarProfesor(request,id):
    
    if request.method == 'POST':
        
        profesor = Profesor.objects.get(id=id)
        profesor.delete()
        profesores=Profesor.objects.all()
        return render(request,"leerProfesores.html",{"profesores": profesores})


def editar_profesor(request,id):
    profesor = Profesor.objects.get(id=id)
        
    if request.method == 'POST':
        
        mi_formulario = ProfesorFormulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            
            profesor.nombre = data['nombre']
            profesor.apellido = data['apellido']
            profesor.email = data['email']
            profesor.profesion = data['profesion']
            profesor.save()
            return redirect('ListaProfesores')
    else:
        mi_formulario = ProfesorFormulario(initial={"nombre": profesor.nombre,"apellido": profesor.apellido,"email":profesor.email,"profesion":profesor.profesion})
    return render(request,"editarProfesor.html", {'mi_formulario': mi_formulario, 'id':profesor.id})

    
class CursoLista(ListView):
    
    model = Curso
    
    template_name = 'curso_list.html' 
    
    context_object_name = "cursos"
        
class CursoDetail(DetailView):
    
    model = Curso
    
    template_name = 'curso_detail.html' 
    
    context_object_name = "curso"

class CursoCreate(CreateView):
    
    model = Curso
    
    template_name = 'curso_create.html'
    
    fields = ('__all__')
    success_url = '/app-coder/'
    

class CursoUpdate(UpdateView):
    
    model = Curso
    
    template_name = 'curso_update.html'
    
    fields = ('__all__')
    success_url = '/app-coder/'
    

class CursoDelete(DeleteView):
    
    model = Curso
    
    template_name = 'curso_delete.html' 
    
    success_url = '/app-coder/'


        
    
            
    