from django.urls import path, re_path
from . import views

app_name = "invoices"

urlpatterns = [
    path("create/", views.InvoiceCreateView.as_view(), name="create_invoice"),
    re_path(
        r"^edit/(?P<invoice_id>[0-9a-f-]+)/$", views.EditInvoices, name="edit_invoice"
    ),  # Utilisation de re_path pour UUID
    path(
        "generate-pdf/<uuid:invoice_id>/",
        views.generate_invoice_pdf,
        name="generate_pdf",
    ),
]
