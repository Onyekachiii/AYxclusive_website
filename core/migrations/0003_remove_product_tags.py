# Generated by Django 4.2.6 on 2023-10-10 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_cartorder_price_alter_cartorderproducts_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
    ]