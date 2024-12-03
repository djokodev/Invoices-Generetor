from django.shortcuts import render
from .models import Customer
from django.views.generic.edit import CreateView
from .forms import CustomerForm
from django.urls import reverse_lazy


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/create_customer.html'
    success_url = reverse_lazy('dashboard') 