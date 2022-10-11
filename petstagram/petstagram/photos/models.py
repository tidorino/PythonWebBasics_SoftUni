from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet


class Photo(models.Model):
    MAX_DESCRIPTION_LENGTH = 300
    MIN_DESCRIPTION_LENGTH = 10

    LOCATION_MAX_LEN = 30

    photo = models.ImageField(
        null=False,
        blank=True,
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
        null=True,
        blank=True,
    )

    location = models.CharField(
        max_length=LOCATION_MAX_LEN,
        null=True,
        blank=True,
    )

    publication_date = models.DateField(
        auto_now=True,
        null=False,
        blank=True,
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )
