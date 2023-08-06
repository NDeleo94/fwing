from django.db import models

TIPO = (
    ("p", "Pública"),
    ("e", "Privada"),
    ("i", "Independiente"),
)

EMPLEADOS = (
    (1, "1-10 Empleados (FW)"),
    (2, "11-100 Empleados (FW)"),
    (3, "101-1000+ Empleados (FW)"),
    (4, "1 Empleado (LinkedIn)"),
    (5, "1-10 Empleados (LinkedIn)"),
    (6, "11-50 Empleados (LinkedIn)"),
    (7, "51-200 Empleados (LinkedIn)"),
    (8, "201-500 Empleados (LinkedIn)"),
    (9, "501-1000 Empleados (LinkedIn)"),
    (10, "1001-5000 Empleados (LinkedIn)"),
    (11, "5001-10000 Empleados (LinkedIn)"),
    (12, "10001+ Empleados (LinkedIn)"),
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
