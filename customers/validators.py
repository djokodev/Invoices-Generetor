import re
from django.core.exceptions import ValidationError


def validate_postal_code(value):
    postal_code_regex = r'^\d{4,5}$'
    if not re.match(postal_code_regex, value):
        raise ValidationError("Code postal invalide")