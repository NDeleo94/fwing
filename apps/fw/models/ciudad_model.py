from django.db import models


class Ciudad(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    ciudad = models.CharField(
        max_length=200,
        blank=False,
        null=False,
    )
    lat = models.DecimalField(
        "Latitud",
        max_digits=11,
        decimal_places=8,
        null=True,
        blank=True,
    )
    long = models.DecimalField(
        "Longitud",
        max_digits=11,
        decimal_places=8,
        null=True,
        blank=True,
    )

    estado = models.BooleanField(
        default=True,
    )

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

    def __str__(self) -> str:
        return self.ciudad
