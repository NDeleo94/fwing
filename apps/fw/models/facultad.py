from django.db import models


class Facultad(models.Model):
    id = models.AutoField(primary_key=True)
    facultad = models.CharField(max_length=200, null=False, blank=False)
    acronimo = models.CharField(max_length=25, null=True, blank=True)
    domicilio = models.CharField(max_length=200, null=True, blank=True)
    web = models.URLField(max_length=200, null=True, blank=True)

    estado = models.BooleanField(
        default=True,
        help_text=(
            "Indica si la actividad de la facultad esta vigente. "
            "Por defecto esta activa"
        ),
    )

    email = models.EmailField(max_length=254, null=True, blank=True)
    telefono = models.CharField(max_length=100, null=True, blank=True)

    universidad = models.ForeignKey(
        "Universidad", related_name="facultades", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Facultad"
        verbose_name_plural = "Facultades"
        ordering = ["facultad", "-universidad"]

    def __str__(self) -> str:
        return f"{self.facultad} ({self.universidad.acronimo})"
