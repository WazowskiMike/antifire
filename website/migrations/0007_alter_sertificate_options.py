# Generated by Django 5.1.4 on 2025-01-16 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_alter_sertificate_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sertificate',
            options={'verbose_name': 'Сертификат', 'verbose_name_plural': 'Сертификаты'},
        ),
    ]
