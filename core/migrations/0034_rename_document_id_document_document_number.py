# Generated by Django 4.2.6 on 2023-12-08 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_quotation_is_approved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='document_id',
            new_name='document_number',
        ),
    ]