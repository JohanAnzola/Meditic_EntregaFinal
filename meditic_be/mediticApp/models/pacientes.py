from django.db import models

class Pacientes(models.Model):
    
    idPaciente = models.AutoField(primary_key = True)
    dni = models.CharField('Dni', max_length = 30, unique = True)
    nombres = models.CharField('Nombres', max_length = 50)
    apellidos = models.CharField('Apellidos', max_length = 50)
    edad = models.IntegerField('Edad')
    entidad = models.CharField('Entidad', max_length = 50)
    telefono = models.CharField('Telefono', max_length = 45)
    correo = models.CharField('Correo', max_length = 45)
    enfermedades = models.CharField('Enfermedades', max_length = 256)
    alergias = models.CharField('Alergias', max_length = 256)