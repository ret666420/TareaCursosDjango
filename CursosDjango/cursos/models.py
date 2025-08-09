from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Curso")
    descripcion = models.TextField(verbose_name="Descripción")
    cupo = models.IntegerField(verbose_name="Cupo Máximo")
    costo = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Costo")
    activo = models.BooleanField(default=True, verbose_name="¿Está activo?")
    imagen = models.ImageField(upload_to='cursos/', verbose_name="Imagen del Curso")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['fecha_creacion']  

class nuevoCurso(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Curso")
    descripcion = models.TextField(verbose_name="Descripción")
    cupo = models.IntegerField(verbose_name="Cupo Máximo")
    costo = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Costo")
    activo = models.BooleanField(default=True, verbose_name="¿Está activo?")
    imagen = models.ImageField(upload_to='cursos/', verbose_name="Imagen del Curso")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Nuevo Curso"
        verbose_name_plural = "Nuevos Cursos"
        ordering = ['fecha_creacion']