from django.db import models


class Carrera(models.Model):
    id = models.AutoField(primary_key=True)
    carrera = models.CharField(max_length=200, null=False, blank=False)
    web = models.URLField(max_length=200, null=True, blank=True)
    plan = models.CharField("Plan de estudios", max_length=200, null=False, blank=False)
    acreditacion = models.CharField(
        "Año de acreditación", max_length=200, null=False, blank=False
    )
    acreditadora = models.CharField(
        "Organizacion acreditadora",
        max_length=200,
        null=False,
        blank=False,
        default="CONEAU",
    )

    estado = models.BooleanField(
        default=True,
        help_text=(
            "Indica si la actividad de la carrera esta vigente. "
            "Por defecto esta activa"
        ),
    )

    facultad = models.ForeignKey(
        "Facultad",
        related_name="carreras",
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ["carrera", "facultad"]

    def __str__(self) -> str:
        return f"{self.carrera} ({self.facultad.acronimo if self.facultad.acronimo != None else self.facultad})"
