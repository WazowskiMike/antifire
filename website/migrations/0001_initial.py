# Generated by Django 5.1.4 on 2025-01-14 10:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Основной текст')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
            },
        ),
        migrations.CreateModel(
            name='BlogPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='blog_photos/', verbose_name='Фотография')),
                ('caption', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание фотографии')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='website.blog', verbose_name='Блог')),
            ],
            options={
                'verbose_name': 'Фотография блога',
                'verbose_name_plural': 'Фотографии блога',
            },
        ),
    ]
