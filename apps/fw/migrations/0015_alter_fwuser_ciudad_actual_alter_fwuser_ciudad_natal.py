# Generated by Django 4.1 on 2023-07-15 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("fw", "0014_actividad_ciudad"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fwuser",
            name="ciudad_actual",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="ciudad_actual",
                to="fw.ciudad",
            ),
        ),
        migrations.AlterField(
            model_name="fwuser",
            name="ciudad_natal",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="ciudad_natal",
                to="fw.ciudad",
            ),
        ),
    ]
