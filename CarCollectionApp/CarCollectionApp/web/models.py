from enum import Enum

from django.core.validators import MinLengthValidator
from django.db import models

from CarCollectionApp.web.validators import years_validator, validate_min_age_18, validate_min_price


class Profile(models.Model):
    MAX_LEN_USERNAME = 10
    MIN_LEN_USERNAME = 2

    MAX_PASSWORD_LEN = 30
    MAX_NAME_LEN = 30

    username = models.CharField(
        max_length=MAX_LEN_USERNAME,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(MIN_LEN_USERNAME),
        ),
    )

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            validate_min_age_18,
        ),
    )

    password = models.CharField(
        max_length=MAX_PASSWORD_LEN,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_NAME_LEN,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_NAME_LEN,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Type(Enum):

    SPORTS_CAR = 'Sports Car'
    PICKUP = 'Pickup'
    CROSSOVER = 'Crossover'
    MINIBUS = 'Minibus'
    OTHER = 'Other'

    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class Car(models.Model):
    MAX_TYPE_NAME_LEN = 10
    MAX_MODEL_LEN = 20
    MIN_MODEL_LEN = 2

    type = models.CharField(
        max_length=MAX_TYPE_NAME_LEN,
        choices=Type.choices(),
        null=False,
        blank=False,
    )

    model = models.CharField(
        max_length=MAX_MODEL_LEN,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(MIN_MODEL_LEN),
        ),
    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            years_validator,
        ),
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validate_min_price,
        ),
    )
