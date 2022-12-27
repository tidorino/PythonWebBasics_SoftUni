import re

from django.core.exceptions import ValidationError


def validate_first_name_start_with_capital_letter(value):
    if value[0].isupper():
        return value
    raise ValidationError('Your name must start with a capital letter!')


def validate_only_letters(value):
    pattern = "^[A-Za-z]*$"
    state = bool(re.match(pattern, value))
    if not state:
        raise ValidationError('Plant name should contain only letters!')
    return value
