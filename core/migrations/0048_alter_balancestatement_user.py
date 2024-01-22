# Generated by Django 4.2.6 on 2024-01-19 21:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0047_invoice_proof_of_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balancestatement',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
