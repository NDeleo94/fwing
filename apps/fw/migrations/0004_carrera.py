# Generated by Django 4.1 on 2023-04-24 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("fw", "0003_facultad"),
    ]

    operations = [
        migrations.CreateModel(
            name="Carrera",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("carrera", models.CharField(max_length=200)),
                ("web", models.URLField(blank=True, null=True)),
                (
                    "following",
                    models.BooleanField(
                        default=True,
                        help_text="Indica si el sistema realiza seguimiento de la carrera. Por defecto esta inactiva",
                    ),
                ),
                (
                    "estado",
                    models.BooleanField(
                        default=True,
                        help_text="Indica si la actividad de la carrera esta vigente. Por defecto esta activa",
                    ),
                ),
                (
                    "facultad",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="carreras",
                        to="fw.facultad",
                    ),
                ),
            ],
            options={
                "ordering": ["carrera", "facultad"],
            },
        ),
    ]
