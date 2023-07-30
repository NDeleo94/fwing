from django.db import models
from ckeditor.fields import RichTextField


class Email(models.Model):
    plantilla = models.CharField(max_length=100)
    asunto = models.CharField(max_length=200)
    cuerpo = RichTextField()
    estado = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return self.plantilla
