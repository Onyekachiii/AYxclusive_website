# Generated by Django 4.2.6 on 2023-11-29 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_projectimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='payment_status',
            field=models.CharField(choices=[('unpaid', 'Unpaid'), ('paid', 'Paid'), ('part_paid', 'Part-Paid')], default='unpaid', max_length=20),
        ),
        migrations.AddField(
            model_name='quotation',
            name='payment_status',
            field=models.CharField(choices=[('unpaid', 'Unpaid'), ('paid', 'Paid'), ('part_paid', 'Part-Paid')], default='unpaid', max_length=20),
        ),
        migrations.AddField(
            model_name='receipts',
            name='payment_status',
            field=models.CharField(choices=[('unpaid', 'Unpaid'), ('paid', 'Paid'), ('part_paid', 'Part-Paid')], default='unpaid', max_length=20),
        ),
    ]
