from django.db import models


class Actividad(models.Model):
    id = models.AutoField(primary_key=True)

    usuario = models.ForeignKey(
        "FwUser", related_name="historial", on_delete=models.CASCADE
    )
    organizacion = models.ForeignKey(
        "Organizacion", related_name="actividades", on_delete=models.CASCADE
    )
    puesto = models.ForeignKey(
        "Puesto", related_name="actividades", on_delete=models.CASCADE
    )
    ciudad = models.ForeignKey(
        "Ciudad",
        related_name="actividades",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    inicio = models.DateField("Inicio de actividad", blank=False, null=False)
    fin = models.DateField("Fin de actividad", blank=True, null=True)
    estado = models.BooleanField(
        default=True,
    )

    class Meta:
        verbose_name = "Actividad Laboral"
        verbose_name_plural = "Actividades Laborales"

        ordering = [
            "fin",
            "-inicio",
        ]

    def __str__(self) -> str:
        return f"Actividad"
