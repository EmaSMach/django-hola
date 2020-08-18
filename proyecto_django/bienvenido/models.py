from django.db import models

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    nacimiento = models.DateField()
    sueldo = models.DecimalField(decimal_places=2, max_digits=10)
    departamento = models.ForeignKey(Departamento, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre
