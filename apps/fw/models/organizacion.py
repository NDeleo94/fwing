from django.db import models

TIPO = (
    ("p", "Pública"),
    ("e", "Privada"),
    ("i", "Independiente"),
)


class Organizacion(models.Model):
    id = models.AutoField(primary_key=True)
    organizacion = models.CharField(
        "Organizacion", max_length=200, blank=False, null=False
    )
    tipo = models.CharField(
        max_length=200,
        choices=TIPO,
        blank=True,
        help_text="Organizacion pública, privada o trabajo independiente",
    )
    descripcion = models.TextField(max_length=255, blank=True, null=True)
    estado = models.BooleanField(default=True)
    email = models.EmailField(blank=True, null=True)
    # telefono = models.CharField(maxblank=True, null=True)
    web = models.URLField("Sitio Web", blank=True, null=True)

    class Meta:
        verbose_name = "Organizacion"
        verbose_name_plural = "Organizaciones"

    def __str__(self) -> str:
        return self.organizacion
