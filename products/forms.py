from django import forms
from .models import Category, Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "brand", "reference", "category", "description", "price"]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
