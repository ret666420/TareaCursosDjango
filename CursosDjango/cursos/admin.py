from django.contrib import admin
from .models import Curso
from .models import nuevoCurso
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'costo', 'cupo', 'activo', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('activo', ('fecha_creacion', admin.DateFieldListFilter))
    readonly_fields = ('fecha_creacion',)

    fieldsets = (
        ('Información General', {
            'fields': ('nombre', 'descripcion', 'imagen')
        }),
        ('Detalles del Curso', {
            'fields': ('cupo', 'costo', 'activo')
        }),
        ('Metadatos', {
            'fields': ('fecha_creacion',)
        }),
    )

class nuevoCursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'costo', 'cupo', 'activo', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('activo', ('fecha_creacion', admin.DateFieldListFilter))
    readonly_fields = ('fecha_creacion',)

admin.site.register(nuevoCurso, nuevoCursoAdmin)