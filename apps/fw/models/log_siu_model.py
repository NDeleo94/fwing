from django.db import models


class LogSIU(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.IntegerField(
        "Cantidad de egresados",
        blank=False,
        null=False,
    )
    origen = models.IntegerField(
        "Actualización",
        choices=(
            (1, "AUTO"),
            (2, "MANUAL"),
        ),
        blank=False,
        null=False,
    )
    fecha = models.DateField(
        "Fecha de Actualización",
        auto_now_add=True,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = "Log de SIU"
        verbose_name_plural = "Log de SIU"
