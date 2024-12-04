from django.contrib import admin
from .models import Invoice, InvoiceProduct



admin.site.register(Invoice)
admin.site.register(InvoiceProduct)