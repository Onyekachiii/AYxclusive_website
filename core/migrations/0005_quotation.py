# Generated by Django 4.2.6 on 2023-11-14 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quotation_number', shortuuid.django_fields.ShortUUIDField(alphabet='abc12345678', length=10, max_length=20, prefix='quo_', unique=True)),
                ('file', models.FileField(upload_to='quotations/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('email_subject', models.CharField(max_length=255)),
                ('email_body', models.TextField()),
                ('sent', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
