from django.shortcuts import render, redirect 
from .models import Curso
from .forms import CursoForm 
from django.shortcuts import get_object_or_404


def index(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos.html', {'cursos': cursos})

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cursos') 
    else:
        form = CursoForm()
    return render(request, 'registros/crear_curso.html', {'form': form})

def cursos(reques): 
    return render(reques, 'cursos/cursos.html')

def confirmarEliminacion(request, id, confirmacion='cursos/confirmarEliminacion.html'):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        curso.delete()
        return redirect('cursos')   # O usa redirect('/cursos/')
    return render(request, confirmacion, {'curso': curso})


def editar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursos')  # Redirige al listado de cursos
    else:
        form = CursoForm(instance=curso)
    
    return render(request, "cursos/formEditarCurso.html", {
        'form': form,
        'curso': curso
    })