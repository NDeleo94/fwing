# Generated by Django 4.1 on 2023-09-07 01:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fw", "0016_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="fwuser",
            name="linkedin_id",
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name="LinkedIn ID"
            ),
        ),
    ]
