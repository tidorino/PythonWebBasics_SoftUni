from django.core.exceptions import ValidationError


def years_validator(value):
    if 1980 <= value <= 2049:
        return value
    raise ValidationError('Year must be between 1980 and 2049')


def validate_min_age_18(value):
    if value < 18:
        raise ValidationError('The age cannot be below 18')
    return value


def validate_min_price(value):
    if value < 1:
        raise ValidationError('Price cannot be below 1')
    return value

