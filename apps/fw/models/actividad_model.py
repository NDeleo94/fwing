from django.db import models

MODALIDAD = (
    (1, "Presencial"),
    (2, "Hibrido"),
    (3, "Remoto"),
)

SENIORITY = (
    (1, "Trainee"),
    (2, "Junior"),
    (3, "Semi-Senior"),
    (4, "Senior"),
    (5, "Director"),
    (6, "Vice Presidente"),
    (7, "Jefe"),
)


class Actividad(models.Model):
    id = models.AutoField(primary_key=True)

    usuario = models.ForeignKey(
        "FwUser",
        related_name="historial",
        on_delete=models.CASCADE,
    )
    organizacion = models.ForeignKey(
        "Organizacion",
        related_name="actividades",
        on_delete=models.CASCADE,
    )
    puesto = models.ForeignKey(
        "Puesto",
        related_name="actividades",
        on_delete=models.CASCADE,
    )
    ciudad = models.ForeignKey(
        "Ciudad",
        related_name="actividades",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    modalidad = models.IntegerField(
        choices=MODALIDAD,
        blank=True,
        null=True,
    )
    seniority = models.IntegerField(
        choices=SENIORITY,
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
