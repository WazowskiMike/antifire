# Generated by Django 5.0.4 on 2025-01-22 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0010_alter_blog_content"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200, verbose_name="Название")),
                ("price", models.IntegerField()),
                ("photo", models.ImageField(upload_to="products/")),
            ],
        ),
    ]
