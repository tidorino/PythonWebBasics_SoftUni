# from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MinLengthValidator, MaxValueValidator
from django.db import models

#
# def validate_min_characters(value):
#     if value < 2:
#         raise ValidationError('The username must be a minimum of 2 chars')
#     return value


class Profile(models.Model):
    USERNAME_MAX_LEN = 10
    USERNAME_MIN_LEN = 2
    MIN_AGE_VALUE = 18

    PASSWORD_MAX_LEN = 30
    NAME_MAX_LEN = 30

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(USERNAME_MIN_LEN),
        ),
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(MIN_AGE_VALUE),
        ),
    )

    password = models.CharField(
        max_length=PASSWORD_MAX_LEN,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=NAME_MAX_LEN,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=NAME_MAX_LEN,
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


class Car(models.Model):
    TYPE_MAX_LEN = 10

    MODEL_MAX_LEN = 20
    MODEL_MIN_LEN = 2

    MIN_YEAR = 1980
    MAX_YEAR = 2049

    PRICE_MIN_VALUE = 1

    SPORTS_CAR = 'Sports Car'
    PICKUP_CAR = 'Pickup'
    CROSSOVER = 'Crossover'
    MINIBUS = 'Minibus'
    OTHER = 'Other'

    CHOICES = (
        (SPORTS_CAR, SPORTS_CAR),
        (PICKUP_CAR, PICKUP_CAR),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER),
    )

    type = models.CharField(
        max_length=TYPE_MAX_LEN,
        null=False,
        blank=False,
        choices=CHOICES,
    )

    model = models.CharField(
        max_length=MODEL_MAX_LEN,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(MODEL_MIN_LEN),
        ),
    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(MIN_YEAR),
            MaxValueValidator(MAX_YEAR),
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
            MinValueValidator(PRICE_MIN_VALUE),
        ),
    )
