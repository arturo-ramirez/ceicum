from django.db import models

# Create your models here.


class Generacion(models.Model):
    generacion = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Generación'
        verbose_name_plural = "Generación"

    def __str__(self):
        return self.generacion


class Curso(models.Model):
    numero_g = models.ForeignKey(
        Generacion, on_delete=models.CASCADE, blank=True, null=True)
    nombre_curso = models.CharField(
        max_length=100)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = "Curso"

    def __str__(self):
        return self.nombre_curso
