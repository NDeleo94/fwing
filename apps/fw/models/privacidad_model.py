from django.db import models


class Privacidad(models.Model):
    dni = models.BooleanField(
        verbose_name="Mostrar numero de documento",
        default=True,
    )
    email = models.BooleanField(
        verbose_name="Mostrar correo electronico",
        default=True,
    )
    nombres = models.BooleanField(
        verbose_name="Mostrar nombres",
        default=True,
    )
    apellidos = models.BooleanField(
        verbose_name="Mostrar apellidos",
        default=True,
    )
    fecha_nac = models.BooleanField(
        verbose_name="Mostrar fecha de nacimiento",
        default=True,
    )
    nacionalidad = models.BooleanField(
        verbose_name="Mostrar nacionalidad",
        default=True,
    )
    ciudad_natal = models.BooleanField(
        verbose_name="Mostrar ciudad natal",
        default=True,
    )
    ciudad_actual = models.BooleanField(
        verbose_name="Mostrar ciudad actual",
        default=True,
    )
    domicilio = models.BooleanField(
        verbose_name="Mostrar domicilio",
        default=False,
    )
    certificado = models.BooleanField(
        verbose_name="Mostrar certificado",
        default=False,
    )
    sexo = models.BooleanField(
        verbose_name="Mostrar sexo",
        default=True,
    )
    egresado = models.ForeignKey(
        "FwUser", related_name="privacidad", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Privacidad"
        verbose_name_plural = "Privacidades"
