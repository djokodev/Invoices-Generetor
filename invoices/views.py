from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.shortcuts import HttpResponse
from .models import Invoice, InvoiceProduct
from products.models import Product
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML


class InvoiceCreateView(LoginRequiredMixin, CreateView):
    model = Invoice
    template_name = "invoices/create_invoice.html"
    fields = ["customer"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        invoice = form.save()
        return redirect("invoices:edit_invoice", invoice_id=invoice.id)


def delete_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id, user=request.user)
    invoice.delete()
    return redirect("invoices:draft_invoices")


def draft_invoices_view(request):
    drafts = Invoice.objects.filter(status="draft", user=request.user)
    return render(request, "invoices/draft_invoices.html", {"drafts": drafts})


def edit_invoices(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)

    if request.method == "POST":

        if request.POST.get("action") == "save_draft":
            invoice.status = "draft"
            invoice.save()
            return redirect("invoices:draft_invoices")
    
        if request.POST.get("action") == "remove":
            line_id = request.POST.get("line_id")
            if line_id:
                line = get_object_or_404(InvoiceProduct, id=line_id, invoice=invoice)
                line.delete()
                invoice.update_total()

        else:
            product_id = request.POST.get("product")
            quantity = int(request.POST.get("quantity", 1))
            if product_id:
                product = get_object_or_404(Product, id=product_id)
                InvoiceProduct.objects.create(
                    invoice=invoice,
                    product=product,
                    quantity=quantity,
                    unit_price=product.price,
                    tva=product.tva,
                )
                invoice.update_total()

    products = Product.objects.all()

    context = {
        "invoice": invoice,
        "products": products,
    }
    return render(request, "invoices/edit_invoice.html", context=context)


def generate_invoice_pdf(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)

    html_string = render_to_string("invoices/pdf_template.html", {"invoice": invoice})

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="facture_{invoice.id}.pdf"'

    HTML(string=html_string).write_pdf(response)

    return response
