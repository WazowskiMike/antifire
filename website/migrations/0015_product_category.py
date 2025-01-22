# Generated by Django 5.0.4 on 2025-01-22 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0014_alter_product_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[
                    ("fire_doors", "Противопожарные двери"),
                    ("fire_hatches", "Противопожарные люки"),
                    ("fire_gates", "Противопожарные ворота"),
                    ("aluminum_structures", "Алюминиевые конструкции"),
                    ("hidden_doors", "Скрытые двери"),
                    ("ultra_clear_structures", "Сверхпрозрачные конструкции"),
                    ("technical_products", "Технические изделия"),
                ],
                default=0,
                max_length=50,
                verbose_name="Категория",
            ),
            preserve_default=False,
        ),
    ]