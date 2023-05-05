from django.db import models
from apps.fw.models.carrera_model import Carrera
from apps.fw.models.user_model import FwUser


class Egreso(models.Model):
    carrera = models.ForeignKey(
        Carrera,
        related_name="carreras",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    usuario = models.ForeignKey(
        FwUser,
        related_name="egresos",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    ciclo_egreso = models.DateField("Año de Egreso", blank=True, null=True)
    matricula = models.CharField("Matricula", max_length=50, blank=True, null=True)
    estado = models.BooleanField(
        default=True,
    )

    class Meta:
        db_table = "fw_egresado_carrera"
        verbose_name = "Egreso"
        verbose_name_plural = "Egresos"

        ordering = [
            "ciclo_egreso",
        ]

    def __str__(self) -> str:
        return self.usuario.__str__()
