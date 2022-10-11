from django.core.validators import URLValidator
from django.db import models
from django.template.defaultfilters import slugify


class Pet(models.Model):
    MAX_LENGTH_NAME = 30

    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        null=False,
        blank=False
    )

    personal_pet_photo = models.URLField(
        null=False,
        blank=False,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=False,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(
                f'{self.id}-{self.name}'
            )
        return super().save(*args, **kwargs)
