from django.urls import path, re_path
from . import views

app_name = "invoices"

urlpatterns = [
    path("create/", views.InvoiceCreateView.as_view(), name="create_invoice"),
    path("draft-invoices/", views.draft_invoices_view, name="draft_invoices"),
    path("delete/<uuid:invoice_id>/", views.delete_invoice, name="delete_invoice"),
    re_path(
        r"^edit/(?P<invoice_id>[0-9a-f-]+)/$", views.edit_invoices, name="edit_invoice"
    ),  # Utilisation de re_path pour UUID
    path("generate-pdf/<uuid:invoice_id>/", views.generate_invoice_pdf, name="generate_pdf"),
]
