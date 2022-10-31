from django.urls import path

from appcoder.views import curso1,inicio
from appcoder.views import lista_curso,Cursos2,Profesores2,Entregables2,Estudiantes2,cursoFormulario,busqueda_camada,buscar


urlpatterns = [
    path("", inicio),
    path("agregar-curso/<nombre1>/<camada1>", curso1),
    path("lista-cursos", lista_curso),
    path("Cursos", Cursos2, name="Cursos"),
    path("profesores", Profesores2, name="Profesores"),
    path("Entregables", Entregables2),
    path("Estudiantes", Estudiantes2,name="Estudiantes"),
    path("cursoFormulario/", cursoFormulario, name = "CursoFormulario"),
    path('busqueda_camada/', busqueda_camada, name = 'busqueda_camada'),
    path('buscar', buscar, name = 'buscar'),
]
