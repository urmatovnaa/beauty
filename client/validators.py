from django.core.exceptions import ValidationError


def validate_english(text):
    if not bool(text.isascii()):
        raise ValidationError(
            'Use only english letters',
        )
