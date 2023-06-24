from django.db import models


class Imagen(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.ImageField(
        blank=True,
        null=True,
        upload_to="images/",
        verbose_name="Imagen Perfil",
    )
    url = models.URLField(
        blank=True,
        null=True,
        verbose_name="URL Imagen Perfil",
    )
    usuario = models.ForeignKey(
        "FwUser",
        related_name="imagen",
        on_delete=models.CASCADE,
    )
    estado = models.BooleanField(
        default=True,
    )

    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Imagenes"

    def __str__(self) -> str:
        return f"Imagen de Perfil"
