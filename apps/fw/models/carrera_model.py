from django.db import models
from apps.fw.models.user_model import FwUser


class Carrera(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    carrera = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )
    web = models.URLField(
        max_length=200,
        null=True,
        blank=True,
    )
    following = models.BooleanField(
        default=False,
        help_text="Indica si el sistema realiza seguimiento de la carrera. Por defecto esta inactiva",
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

    egresado = models.ManyToManyField(
        FwUser,
        related_name="carreras",
        through="Egreso",
        blank=True,
    )

    class Meta:
        ordering = ["carrera", "facultad"]

    def __str__(self) -> str:
        return (
            f"{self.carrera} ({self.facultad.acronimo})"
            if self.facultad.acronimo != None
            else f"{self.carrera} ({self.facultad.facultad})"
        )


class Titulo(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    titulo = models.CharField(
        max_length=200,
    )

    estado = models.BooleanField(
        default=True,
        help_text=(
            "Indica si la actividad del titulo esta vigente. " "Por defecto esta activa"
        ),
    )

    carrera = models.ForeignKey(
        "Carrera",
        related_name="titulos",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Titulo Intermedio"
        verbose_name_plural = "Titulos Intermedios"

    def __str__(self) -> str:
        return self.titulo


class Plan(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    plan = models.CharField(
        "Plan de estudios",
        max_length=200,
        null=False,
        blank=False,
    )
    acreditacion = models.CharField(
        "Año de acreditación",
        max_length=200,
        null=False,
        blank=False,
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
            "Indica si la actividad del titulo esta vigente. " "Por defecto esta activa"
        ),
    )

    carrera = models.ForeignKey(
        "Carrera",
        related_name="planes",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Plan"
        verbose_name_plural = "Planes"

    def __str__(self) -> str:
        return f"{self.carrera} {self.plan}"
