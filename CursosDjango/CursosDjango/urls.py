"""
URL configuration for CursosDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from contenido import views
from django.conf import settings
from django.conf.urls.static import static
from cursos import views as views_cursos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('crear/', views.crear, name='crear'),
    path('cursos/', include('cursos.urls')),
    path('crear_curso/', views_cursos.crear_curso, name='crear_curso'),
    path('cursos/confirmarEliminacion/<int:id>/', views_cursos.confirmarEliminacion, name='confirmarEliminacion'),
    path('cursos/editar/<int:id>/', views_cursos.editar_curso, name='editar_curso'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
