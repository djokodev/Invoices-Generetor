from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from .validators import validate_postal_code


class Customer(models.Model):
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    address = models.CharField()
    postal_code = models.CharField(max_length=20, validators=[validate_postal_code])
    city = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = PhoneNumberField()

    def __str__(self) -> str:
        return f"{self.name} {self.first_name}"
