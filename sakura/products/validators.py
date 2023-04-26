from django.core.exceptions import ValidationError


def number_of_pages_validator(value):
    if value < 50 or value > 5000:
        raise ValidationError(
            'Количество страниц в книге не может быть меньше 50 и больше 5000 тысяч.'
        )
