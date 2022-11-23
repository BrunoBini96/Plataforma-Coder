from django.urls import path

from appcoder.views import curso1,inicio, listaProfesores,crea_profesor
from appcoder.views import lista_curso,Cursos2,Profesores2,Entregables2,Estudiantes2,cursoFormulario,busqueda_camada,buscar,listaCursos


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
    path('listaCurso/', listaCursos, name = 'ListaCursos'),
    path('listaProfesores/', listaProfesores, name = "ListaProfesores"),
    path('crea-profesor/', crea_profesor, name = "CreaProfesor"),
    
]
