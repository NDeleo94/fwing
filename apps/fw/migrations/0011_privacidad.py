# Generated by Django 4.1 on 2023-06-20 23:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("fw", "0010_plan"),
    ]

    operations = [
        migrations.CreateModel(
            name="Privacidad",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "dni",
                    models.BooleanField(
                        default=True, verbose_name="Mostrar numero de documento"
                    ),
                ),
                (
                    "email",
                    models.BooleanField(
                        default=True, verbose_name="Mostrar correo electronico"
                    ),
                ),
                (
                    "nombres",
                    models.BooleanField(default=True, verbose_name="Mostrar nombres"),
                ),
                (
                    "apellidos",
                    models.BooleanField(default=True, verbose_name="Mostrar apellidos"),
                ),
                (
                    "fecha_nac",
                    models.BooleanField(
                        default=True, verbose_name="Mostrar fecha de nacimiento"
                    ),
                ),
                (
                    "nacionalidad",
                    models.BooleanField(
                        default=True, verbose_name="Mostrar nacionalidad"
                    ),
                ),
                (
                    "ciudad_natal",
                    models.BooleanField(
                        default=True, verbose_name="Mostrar ciudad natal"
                    ),
                ),
                (
                    "ciudad_actual",
                    models.BooleanField(
                        default=True, verbose_name="Mostrar ciudad actual"
                    ),
                ),
                (
                    "domicilio",
                    models.BooleanField(
                        default=False, verbose_name="Mostrar domicilio"
                    ),
                ),
                (
                    "certificado",
                    models.BooleanField(
                        default=False, verbose_name="Mostrar certificado"
                    ),
                ),
                (
                    "sexo",
                    models.BooleanField(default=True, verbose_name="Mostrar sexo"),
                ),
                (
                    "egresado",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="privacidad",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Configuracion de Privacidad",
                "verbose_name_plural": "Configuraciones de Privacidad",
            },
        ),
    ]
