from django.db import models
from curso.models import Curso, Generacion
from django.utils import timezone


class Alumno(models.Model):
    curso = models.ForeignKey(
        Curso, on_delete=models.CASCADE, blank=True, null=True)

    generacion = models.ForeignKey(
        Generacion, on_delete=models.CASCADE, blank=True, null=True, related_name='+')

    alumnx = models.CharField(
        max_length=200, blank=True, null=True, verbose_name='Nombre')
    email = models.CharField(max_length=50, blank=True, null=True)
    pais = models.CharField(max_length=20, blank=True,
                            null=True, verbose_name='País')
    bio = models.CharField(max_length=250, blank=True, null=True)
    # Campo con formato anterior, sin "from django.utils import timezone". En caso de habilitar se debe correr makemigrations y migrate.
    # fecha_inscripcion = models.DateField(
    #     auto_now=True, verbose_name='Fecha de inscripción')
    fecha_inscripcion = models.DateField(
        default=timezone.now, verbose_name='Fecha de inscripción')
    img_pago = models.ImageField(
        verbose_name='Imagen pago', upload_to='pagos', blank=True, null=True)
    codigo = models.CharField(
        max_length=20, blank=True, null=True, verbose_name='Código')
    clave = models.CharField(
        max_length=20, blank=True, null=True, verbose_name='Clave')

    class Meta:
        verbose_name = 'Alumnx'
        verbose_name_plural = "Alumnx"

    def __str__(self):
        return self.alumnx
