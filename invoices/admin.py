from django.contrib import admin
from .models import Invoice, InvoiceLine



admin.site.register(Invoice)
admin.site.register(InvoiceLine)