from django.urls import path

from appcoder.views import curso1,inicio, listaProfesores,crea_profesor,eliminarProfesor,editar_profesor,CursoLista,CursoDetail,CursoCreate,CursoDelete,CursoUpdate
from appcoder.views import lista_curso,Cursos2,Profesores2,Entregables2,Estudiantes2,cursoFormulario,busqueda_camada,buscar,listaCursos


urlpatterns = [
    path("", inicio , name = 'Inicio'),
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
    path('elimina-profesor/<int:id>', eliminarProfesor, name = "EliminaProfesor"),
    path('edita-profesor/<int:id>', editar_profesor, name = "EditarProfesor"),
    path('listaCursos/', CursoLista.as_view(), name = "ListaCursos"),
    path('detalleCurso/<pk>', CursoDetail.as_view(), name = "DetalleCurso"),
    path('creaCurso/', CursoCreate.as_view(), name = "CreaCurso"),
    path('actualizarCurso/<pk>', CursoUpdate.as_view(), name = "ActualizaCursos"),
     path('eliminarCurso/<pk>', CursoDelete.as_view(), name = "EliminaCursos"),
]

