from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *

# Vistas para Libro
def libro_list(request):
    libros = Libro.objects.all()
    return render(request, 'libro_list.html', {'libros': libros})

def index(request):
    return render(request, 'index.html')

def libro_create(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libro_list')
    else:
        form = LibroForm()
    return render(request, 'libro_form.html', {'form': form})

def libro_update(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('libro_list')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libro_form.html', {'form': form})

def libro_delete(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('libro_list')
    return render(request, 'libro_confirm_delete.html', {'libro': libro})

# Vistas para Miembro
def miembro_list(request):
    miembros = Miembro.objects.all()
    return render(request, 'miembro_list.html', {'miembros': miembros})

def miembro_create(request):
    if request.method == 'POST':
        form = MiembroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('miembro_list')
    else:
        form = MiembroForm()
    return render(request, 'miembro_form.html', {'form': form})

def miembro_update(request, pk):
    miembro = get_object_or_404(Miembro, pk=pk)
    if request.method == 'POST':
        form = MiembroForm(request.POST, instance= miembro)
        if form.is_valid():
            form.save()
            return redirect('miembro_list')
    else:
        form = MiembroForm(instance=miembro)
    return render(request, 'miembro_form.html', {'form': form})

def miembro_delete(request, pk):
    miembro = get_object_or_404(Miembro, pk=pk)
    if request.method == 'POST':
        miembro.delete()
        return redirect('miembro_list')
    return render(request, 'miembro_confirm_delete.html', {'miembro': miembro})

# Vistas para Prestamo
def prestamo_list(request):
    prestamos = Prestamo.objects.all()
    return render(request, 'prestamo_list.html', {'prestamos': prestamos})

def prestamo_create(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prestamo_list')
    else:
        form = PrestamoForm()
    return render(request, 'prestamo_form.html', {'form': form})

def prestamo_update(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    if request.method == 'POST':
        form = PrestamoForm(request.POST, instance=prestamo)
        if form.is_valid():
            form.save()
            return redirect('prestamo_list')
    else:
        form = PrestamoForm(instance=prestamo)
    return render(request, 'prestamo_form.html', {'form': form})

def prestamo_delete(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    if request.method == 'POST':
        prestamo.delete()
        return redirect('prestamo_list')
    return render(request, 'prestamo_confirm_delete.html', {'prestamo': prestamo})