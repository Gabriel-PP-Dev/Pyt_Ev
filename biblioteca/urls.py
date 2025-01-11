"""
URL configuration for biblioteca project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('libros/', views.libro_list, name='libro_list'),
    path('libros/create/', views.libro_create, name='libro_create'),
    path('libros/<int:pk>/update/', views.libro_update, name='libro_update'),
    path('libros/<int:pk>/delete/', views.libro_delete, name='libro_delete'),

    path('miembros/', views.miembro_list, name='miembro_list'),
    path('miembros/create/', views.miembro_create, name='miembro_create'),
    path('miembros/<int:pk>/update/', views.miembro_update, name='miembro_update'),
    path('miembros/<int:pk>/delete/', views.miembro_delete, name='miembro_delete'),

    path('prestamos/', views.prestamo_list, name='prestamo_list'),
    path('prestamos/create/', views.prestamo_create, name='prestamo_create'),
    path('prestamos/<int:pk>/update/', views.prestamo_update, name='prestamo_update'),
    path('prestamos/<int:pk>/delete/', views.prestamo_delete, name='prestamo_delete'),
]
