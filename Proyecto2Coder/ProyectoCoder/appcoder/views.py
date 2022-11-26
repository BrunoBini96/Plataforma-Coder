from .forms import CursoFormulario, ProfesorFormulario
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from .models import Curso, Profesor
from  django.http import HttpResponse
from django.views.generic import ListView,DeleteView,CreateView,UpdateView,DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required
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

@login_required
def Cursos2(request):
    lista = Curso.objects.all()
    return render(request, "cursos.html", {"lista_cursos" : lista})

@staff_member_required(login_url="/app-coder/login")
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

    
class CursoLista(LoginRequiredMixin,ListView):
    
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

def login2(request):

    if request.method == 'POST':
        
        miFormulario = AuthenticationForm(request, data=request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario = data["username"]
            psw = data["password"]
            
            user = authenticate(username=usuario,password=psw)
            
            if user:
                login(request,user)
                
                return render(request,"inicio.html", {'mensaje': f'Bienvenido {usuario}'})
            else:
                return render(request,"inicio.html", {'mensaje': f'Error datos incorrectos'})
        else:
            return render(request,"inicio.html", {'mensaje': f'Formulario Invalido'})
    
    else:
        miFormulario = AuthenticationForm()
    return render(request,"login.html", {"miFormulario": miFormulario})
   
    
def register(request):

    if request.method == 'POST':
        
        miFormulario = UserCreationForm(request.POST)
        if miFormulario.is_valid():
            username = miFormulario.cleaned_data["username"]
            miFormulario.save()
            return render(request, "inicio.html", {"mensaje": f'Usuario {username} creado con exito'})
        else:
            return render(request, "inicio.html", {"mensaje": f'No se pudo crear el usuario'})

    else:
        miFormulario = UserCreationForm()
    return render(request,"registro.html", {"miFormulario": miFormulario})

    


           
    
            
    