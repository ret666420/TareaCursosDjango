from django import forms
from .models import Curso, nuevoCurso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion', 'cupo', 'costo', 'activo', 'imagen']
      