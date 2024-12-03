from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'first_name', 'address', 'postal_code', 'city', 'email', 'phone']