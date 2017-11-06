from django.db import models

# Create your models here.
from apps.adopcion.models import Persona

class Vacuna(models.Model):
    nombre= models.CharField(max_length=50)
    def __str__(self):
        return '{}'.format(self.nombre)

class Mascota(models.Model):
    #folio = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
    # MANYTOONE
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    # ONETOONE
    # persona= models.OneToOneField(Persona,null=True,blank=True,on_delete=models.CASCADE)
    # MANYTOMANY
    vacuna = models.ManyToManyField(Vacuna)
