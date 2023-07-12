# Generated by Django 4.1 on 2023-07-05 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("fw", "0013_ciudad"),
    ]

    operations = [
        migrations.AddField(
            model_name="actividad",
            name="ciudad",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="actividades",
                to="fw.ciudad",
            ),
        ),
    ]
