# Generated by Django 4.1 on 2023-04-24 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("fw", "0004_carrera"),
    ]

    operations = [
        migrations.CreateModel(
            name="Titulo",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("titulo", models.CharField(max_length=200)),
                (
                    "estado",
                    models.BooleanField(
                        default=True,
                        help_text="Indica si la actividad del titulo esta vigente. Por defecto esta activa",
                    ),
                ),
                (
                    "carrera",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="titulos",
                        to="fw.carrera",
                    ),
                ),
            ],
            options={
                "verbose_name": "Titulo Intermedio",
                "verbose_name_plural": "Titulos Intermedios",
            },
        ),
    ]
