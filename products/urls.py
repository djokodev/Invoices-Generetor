from django.urls import path
from .views import CategoryCreateView, ProductCreateView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path(
        "create-category/",
        login_required(CategoryCreateView.as_view()),
        name="create_category",
    ),
    path(
        "create-product/",
        login_required(ProductCreateView.as_view()),
        name="create_product",
    ),
]
