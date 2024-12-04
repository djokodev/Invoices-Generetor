from .models import Category, Product
from .forms import ProductForm, CategoryForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "products/create_product.html"
    success_url = reverse_lazy("dashboard")


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "products/create_category.html"
    success_url = reverse_lazy("dashboard")
