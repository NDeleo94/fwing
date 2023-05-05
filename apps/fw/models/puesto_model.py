from django.db import models


class Puesto(models.Model):
    id = models.AutoField(primary_key=True)
    puesto = models.CharField(max_length=200, blank=False, null=False)
    descripcion = models.TextField(max_length=255, blank=True, null=True)
    estado = models.BooleanField(
        default=True,
    )

    class Meta:
        verbose_name = "Puesto de trabajo"
        verbose_name = "Puestos de trabajo"

    def __str__(self) -> str:
        return self.puesto
