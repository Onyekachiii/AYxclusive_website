# Generated by Django 4.2.6 on 2023-11-15 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_emailtemplate_receipts_invoice'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoice',
            options={'verbose_name_plural': 'Invoices'},
        ),
        migrations.AlterModelOptions(
            name='quotation',
            options={'verbose_name_plural': 'Quotations'},
        ),
        migrations.AlterModelOptions(
            name='receipts',
            options={'verbose_name_plural': 'Receipts'},
        ),
    ]
