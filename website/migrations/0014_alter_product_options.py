# Generated by Django 5.0.4 on 2025-01-22 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0013_alter_product_photo_alter_product_price"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name": "Продукт", "verbose_name_plural": "Продукты"},
        ),
    ]
