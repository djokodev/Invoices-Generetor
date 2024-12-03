from django.db import models

class Invoice(models.Model):
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

class InvoiceLine(models.Model):
    invoice = models.ForeignKey(Invoice, related_name="lines", on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    tva = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    price_ttc = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


    def calculate_price_ttc(self):
        """Méthode pour calculer le prix TTC."""
        return self.unit_price * (1 + self.tva / 100)

    def save(self, *args, **kwargs):
        """Calcul automatique du prix TTC lors de l'enregistrement."""
        self.price_ttc = self.calculate_price_ttc()
        super().save(*args, **kwargs)
