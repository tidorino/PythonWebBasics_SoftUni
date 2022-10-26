from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.utils.deconstruct import deconstructible


def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError('Ensure this value contains only letters.')
    return value


@deconstructible
class MaxSizeInMbValidator:
    def __int__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.max_size * 1024 * 1024:
            raise ValidationError(f"Max file size is {self.max_size:.2f}MB")


class Profile(models.Model):
    MIN_NAME_LENGTH = 2
    MAX_NAME_LENGTH = 15
    DEFAULT_BUDGET = 0
    BUDGET_MIN_VALUE = 0
    IMAGE_MAX_SIZE_MB = 5
    IMAGE_UPLOAD_TO_DIR = 'profiles/'

    first_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(MIN_NAME_LENGTH),
            validate_only_letters,
        ),
    )

    last_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(MIN_NAME_LENGTH),
            validate_only_letters,
        ),
    )

    budget = models.FloatField(
        default=DEFAULT_BUDGET,
        null=False,
        blank=False,
        validators=(
            MinValueValidator(BUDGET_MIN_VALUE),
        ),
    )

    profile_image = models.ImageField(
        upload_to=IMAGE_UPLOAD_TO_DIR,
        null=True,
        blank=True,
        validators=(
            MaxSizeInMbValidator(IMAGE_MAX_SIZE_MB),
        ),
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Expense(models.Model):
    MAX_LEN_EXPENSE = 30

    title = models.CharField(
        max_length=MAX_LEN_EXPENSE,
        null=False,
        blank=False,
    )

    expense_image = models.URLField()

    price = models.FloatField()

    description = models.TextField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ('title', 'price', 'description',)

