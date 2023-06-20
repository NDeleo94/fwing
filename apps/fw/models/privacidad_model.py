from django.db import models


class Privacidad(models.Model):
    dni = models.BooleanField(
        verbose_name="Numero de documento",
        default=True,
    )
    email = models.BooleanField(
        verbose_name="Correo Electronico",
        default=True,
    )
    nombres = models.BooleanField(
        "Nombres",
        default=True,
    )
    apellidos = models.BooleanField(
        "Apellidos",
        default=True,
    )
    fecha_nac = models.BooleanField(
        "Fecha de Nacimiento",
        default=True,
    )
    nacionalidad = models.BooleanField(
        "Nacionalidad",
        default=True,
    )
    ciudad_natal = models.BooleanField(
        "Ciudad natal",
        default=True,
    )
    ciudad_actual = models.BooleanField(
        "Ciudad actual",
        default=True,
    )
    domicilio = models.BooleanField(
        "Domicilio",
        default=False,
    )
    certificado = models.BooleanField(
        "Certificado",
        default=False,
    )
    sexo = models.BooleanField(
        "Sexo",
        default=True,
    )
    egresado = models.ForeignKey(
        "FwUser", related_name="privacidad", on_delete=models.CASCADE
    )
