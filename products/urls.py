from django.urls import path
from .views import CategoryCreateView, ProductCreateView

urlpatterns = [
    path('create-category/', CategoryCreateView.as_view(), name='create_category'),
    path('create-product/', ProductCreateView.as_view(), name='create_product'),
]
