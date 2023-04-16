from django.db import models


class Universidad(models.Model):
    id = models.AutoField(primary_key=True)
    universidad = models.CharField(max_length=200, null=False, blank=False)
    acronimo = models.CharField(max_length=25, null=True, blank=True)
    domicilio = models.CharField(max_length=200, null=True, blank=True)
    web = models.URLField(max_length=200, null=True, blank=True)

    estado = models.BooleanField(
        default=True,
        help_text=(
            "Indica si la actividad de la universidad esta vigente."
            "Por defecto esta activa"
        ),
    )

    email = models.EmailField(max_length=254, null=True, blank=True)
    telefono = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "Universidad"
        verbose_name_plural = "Universidades"
        ordering = ["-universidad"]

    def __str__(self) -> str:
        return f"{self.universidad} ({self.acronimo})"
