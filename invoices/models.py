from django.db import models
import uuid
from django.contrib.auth import get_user_model

User = get_user_model()


class Invoice(models.Model):
    STATUS_CHOICES = [
        ("draft", "Brouillon"),
        ("validated", "Validée"),
        ("cancelled", "Annulée"),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    @property
    def short_id(self):
        """
        Get a shortened version of the invoice's UUID.

        This property method returns the first 8 characters of the invoice's ID,
        providing a more concise identifier for display or reference purposes.

        Returns:
            str: The first 8 characters of the invoice's UUID.
        """
        return str(self.id)[:8]
    
    customer = models.ForeignKey("customers.Customer", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def update_total(self):
        self.total_price = sum(line.total_price for line in self.lines.all())
        self.save()

    def __str__(self):
        return f"Facture #{self.id} - de Mr/Mm {self.customer.name} {self.customer.first_name}"


class InvoiceProduct(models.Model):
    invoice = models.ForeignKey(Invoice, related_name="lines", on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    tva = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    price_ttc = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def calculate_price_ttc(self):
        return self.unit_price * (1 + self.tva / 100)

    def save(self, *args, **kwargs):
        self.total_price = self.unit_price * self.quantity
        self.price_ttc = self.calculate_price_ttc()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"
