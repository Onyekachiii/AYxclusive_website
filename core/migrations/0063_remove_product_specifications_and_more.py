# Generated by Django 4.2.6 on 2024-02-18 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0062_alter_wallet_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='specifications',
        ),
        migrations.AddField(
            model_name='product',
            name='delivery_time_frame',
            field=models.TextField(blank=True, default='This is the delivery time frame', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='dimensions',
            field=models.TextField(blank=True, default='This is the product dimensions', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='materials',
            field=models.TextField(blank=True, default='This is the product materials', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='structure',
            field=models.TextField(blank=True, default='This is the product structure', null=True),
        ),
    ]