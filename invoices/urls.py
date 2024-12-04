from django.urls import path
from . import views

app_name = "invoices"

urlpatterns = [
    path("create/", views.InvoiceCreateView.as_view(), name="create_invoice"),
    path("edit/<int:invoice_id>/", views.EditInvoices, name="edit_invoice"),
    path("generate-pdf/<int:invoice_id>/", views.generate_invoice_pdf, name="generate_pdf"),
]
