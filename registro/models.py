from django.db import models

# Create your models here.

class Persona(models.Model):
    run = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    correo = models.EmailField(max_length=254)
    telefono = models.IntegerField()
    region = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    vivienda = models.CharField(max_length=100)
    contrasenia = models.CharField(max_length=40)

    def __str(self):
        return "PERSONA"