# Generated by Django 5.1.3 on 2024-12-04 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_invoice_total_price_invoiceproduct_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='status',
            field=models.CharField(choices=[('draft', 'Brouillon'), ('validated', 'Validée'), ('cancelled', 'Annulée')], default='draft', max_length=10),
        ),
    ]