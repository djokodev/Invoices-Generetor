# Generated by Django 5.1.3 on 2024-12-03 03:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0001_initial'),
        ('products', '0002_alter_product_tva'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.CreateModel(
            name='InvoiceProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tva', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('price_ttc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='invoices.invoice')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.DeleteModel(
            name='InvoiceLine',
        ),
    ]
