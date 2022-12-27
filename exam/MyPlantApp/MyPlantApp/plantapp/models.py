from enum import Enum

from django.core.validators import MinLengthValidator
from django.db import models

from MyPlantApp.plantapp.validators import validate_first_name_start_with_capital_letter, validate_only_letters


class Profile(models.Model):
    MAX_LEN_USERNAME = 10
    MIN_LEN_USERNAME = 2

    MAX_LEN_NAME = 20

    username = models.CharField(
        max_length=MAX_LEN_USERNAME,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(MIN_LEN_USERNAME),
        ),
    )

    first_name = models.CharField(
        max_length=MAX_LEN_NAME,
        null=False,
        blank=False,
        validators=(
            validate_first_name_start_with_capital_letter,
        ),
    )

    last_name = models.CharField(
        max_length=MAX_LEN_NAME,
        null=False,
        blank=False,
        validators=(
            validate_first_name_start_with_capital_letter,
        ),
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Type(Enum):

    OUTDOOR_PLANTS = 'Outdoor Plants'
    INDOOR_PLANTS = 'Indoor Plants'

    @classmethod
    def choices(cls):
        return [(p.name, p.value) for p in cls]


class Plant(models.Model):
    MAX_TYPE_LEN = 14

    MAX_PLANT_NAME_LEN = 20
    MIN_PLANT_NAME_LEN = 2

    type = models.CharField(
        max_length=MAX_TYPE_LEN,
        choices=Type.choices(),
        null=False,
        blank=False,
    )

    name = models.CharField(
        max_length=MAX_PLANT_NAME_LEN,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(MIN_PLANT_NAME_LEN),
            validate_only_letters,
        ),
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
    )
