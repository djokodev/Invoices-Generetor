from django.urls import path
from .views import CustomerCreateView

urlpatterns = [
    path('create/', CustomerCreateView.as_view(), name='create_customer'),
]