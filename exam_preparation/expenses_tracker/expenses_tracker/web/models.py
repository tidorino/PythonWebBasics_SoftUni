from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.utils.deconstruct import deconstructible

VALIDATE_ONLY_LETTERS_EXCEPTION_MESSAGE = "Ensure this value contains only letters."


def validate_only_letters(value):
    if not value.isalpha():  # all(c.isalpha() for c in value):
        raise ValidationError(VALIDATE_ONLY_LETTERS_EXCEPTION_MESSAGE)


@deconstructible
class MaxFileSizeInMbValidator:
    def __int__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.__megabytes_to_bytes(self.max_size):
            raise ValidationError(self.__get_exception_message())

    def __get_exception_message(self):
        return f'Max file size is {self.max_size:.2f} MB'

    @staticmethod
    def __megabytes_to_bytes(self, value):
        return value * 1024 * 1024


class Profile(models.Model):
    NAME_MIN_LEN = 2
    NAME_MAX_LEN = 15

    BUDGET_DEFAULT_VALUE = 0
    BUDGET_MIN_VALUE = 0

    IMAGE_MAX_SIZE_MB = 5
    IMAGE_UPLOAD_TO_DIR = 'profile/'

    first_name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=(
            MinLengthValidator(NAME_MIN_LEN),
            validate_only_letters,
        ),
    )

    last_name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=(
            MinLengthValidator(NAME_MIN_LEN),
            validate_only_letters,
        ),
    )

    budget = models.FloatField(
        default=BUDGET_DEFAULT_VALUE,
        validators=(
            MinValueValidator(BUDGET_MIN_VALUE),
        ),
    )

    image = models.ImageField(
        upload_to=IMAGE_UPLOAD_TO_DIR,
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_MB),
        ),
    )


class Expense(models.Model):
    title = models.CharField()
    expense_image = models.URLField()
    description = models.TextField()
    price = models.FloatField()

