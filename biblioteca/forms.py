from django import forms
from .models import Libro, Prestamo,Miembro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'

class MiembroForm(forms.ModelForm):
    class Meta:
        model = Miembro
        fields = '__all__'

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = '__all__'
