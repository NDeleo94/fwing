from django.db import models

TIPO = (
    ("p", "Pública"),
    ("e", "Privada"),
    ("i", "Independiente"),
)

EMPLEADOS = (
    (1, "1 Empleado"),
    (2, "1-10 Empleados"),
    (3, "11-50 Empleados"),
    (4, "51-200 Empleados"),
    (5, "201-500 Empleados"),
    (6, "501-1000 Empleados"),
    (7, "1001-5000 Empleados"),
    (8, "5001-10000 Empleados"),
    (9, "10001+ Empleados"),
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
    empleados = models.IntegerField(
        "Cantidad de empleados",
        choices=EMPLEADOS,
        blank=True,
        null=True,
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
