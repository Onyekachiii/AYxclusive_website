# Generated by Django 4.2.6 on 2024-01-11 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_alter_balancestatement_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartorderproducts',
            name='invoice_no',
        ),
        migrations.AlterField(
            model_name='balancestatement',
            name='balance_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='balancestatement',
            name='invoice_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='balancestatement',
            name='paid_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
