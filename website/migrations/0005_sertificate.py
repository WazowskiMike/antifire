# Generated by Django 5.1.4 on 2025-01-16 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_remove_gallery_created_at_remove_gallery_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='sertificates/')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
