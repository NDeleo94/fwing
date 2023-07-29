# Generated by Django 4.1 on 2023-05-01 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("fw", "0007_puesto"),
    ]

    operations = [
        migrations.CreateModel(
            name="Actividad",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "inicio",
                    models.DateField(
                        blank=False, null=False, verbose_name="Inicio de actividad"
                    ),
                ),
                (
                    "fin",
                    models.DateField(
                        blank=True, null=True, verbose_name="Fin de actividad"
                    ),
                ),
                ("estado", models.BooleanField(default=True)),
                (
                    "organizacion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="actividades",
                        to="fw.organizacion",
                    ),
                ),
                (
                    "puesto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="actividades",
                        to="fw.puesto",
                    ),
                ),
                (
                    "modalidad",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, "Presencial"), (2, "Hibrido"), (3, "Remoto")],
                        null=True,
                    ),
                ),
                (
                    "seniority",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (1, "Trainee"),
                            (2, "Junior"),
                            (3, "Semi-Senior"),
                            (4, "Senior"),
                            (5, "Director"),
                            (6, "Vice Presidente"),
                            (7, "Jefe"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="historial",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Actividad Laboral",
                "verbose_name_plural": "Actividades Laborales",
                "ordering": ["fin", "-inicio"],
            },
        ),
    ]
