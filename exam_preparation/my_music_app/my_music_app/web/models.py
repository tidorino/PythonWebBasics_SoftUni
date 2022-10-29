from django.core import exceptions
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator
from django.db import models


def validate_only_letters_numbers_underscore(value):
    for ch in value:
        if not ch.isalnum() and ch != '_':
            raise exceptions.ValidationError('Ensure this value contains only letters.')
    return value


class Profile(models.Model):
    MAX_LEN_USERNAME = 15
    MIN_LEN_USERNAME = 2
    # ALPHANUMERIC = r'^[A-Za-z0-9_]'
    # MIN_AGE_VALUE = 0

    username = models.CharField(
        max_length=MAX_LEN_USERNAME,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(MIN_LEN_USERNAME),
            validate_only_letters_numbers_underscore,
        ),
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
        # validators=(
        #     MinValueValidator(MIN_AGE_VALUE),
        # ),
    )


class Album(models.Model):
    MAX_LENGTH = 30
    MIN_PRICE_VALUE = 0.0

    POP_MUSIC = 'Pop Music'
    JAZZ_MUSIC = 'Jazz Music'
    RB_MUSIC = 'R&B Music'
    ROCK_MUSIC = 'Rock Music'
    COUNTRY_MUSIC = 'Country Music'
    DANCE_MUSIC = 'Dance Music'
    HIPHOP_MUSIC = 'Hip Hop Music'
    OTHER = 'Other'
    CHOICES = (
        (POP_MUSIC, POP_MUSIC),
        (JAZZ_MUSIC, JAZZ_MUSIC),
        (RB_MUSIC, 'R&B Music'),
        (ROCK_MUSIC, 'Rock Music'),
        (COUNTRY_MUSIC, 'Country Music'),
        (DANCE_MUSIC, 'Dance Music'),
        (HIPHOP_MUSIC, 'Hip Hop Music'),
        (OTHER, 'Other')
    )

    album_name = models.CharField(
        max_length=MAX_LENGTH,
        unique=True,
        null=False,
        blank=False,
    )

    artist = models.CharField(
        max_length=MAX_LENGTH,
        null=False,
        blank=False,
    )

    genre = models.CharField(
        max_length=MAX_LENGTH,
        null=False,
        blank=False,
        choices=CHOICES,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(MIN_PRICE_VALUE),
        ),
    )

    class Meta:
        ordering = ('pk',)
