from django.db import models

class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.titulo

class Miembro(models.Model):
    id_miembro = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    CI = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre

class Prestamo(models.Model):
    id_prestamo = models.AutoField(primary_key=True)
    libro = models.ForeignKey(Libro, null=True, blank=True, on_delete=models.CASCADE)
    miembro = models.ForeignKey(Miembro, null=True, blank=True, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_devolucion = models.DateField()
    estado = models.CharField(max_length=50, choices=[
        ('PENDIENTE', 'Pendiente'),
        ('DEVUELTO', 'Devuelto'),
        ('RETRASADO', 'Retrasado'),
    ])

    def __str__(self):
        return f"Préstamo {self.id_prestamo} - {self.libro.titulo} a {self.miembro.nombre}"