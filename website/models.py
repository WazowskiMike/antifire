from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField

class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    slug = models.SlugField(max_length=200, unique=True,blank=True) 
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"

    def __str__(self):
        return self.title


class BlogPhoto(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="photos")
    photo = models.ImageField(upload_to="blog_photos/")  # Загруженные файлы будут храниться в media/blog_photos/
    caption = models.CharField(max_length=255, blank=True, null=True)

class Gallery(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название галереи")

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галереи"

    def __str__(self):
        return self.title

class GalleryPhoto(models.Model):
    gallery = models.ForeignKey(
        Gallery,
        on_delete=models.CASCADE,
        related_name="photos",
        verbose_name="Галерея"
    )
    photo = models.ImageField(upload_to="gallery_photos/", verbose_name="Фотография")
    caption = models.CharField(max_length=255, blank=True, verbose_name="Описание фото")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")

    class Meta:
        verbose_name = "Фотография галереи"
        verbose_name_plural = "Фотографии галереи"

    def __str__(self):
        return f"Фото из {self.gallery.title} - {self.caption or 'Без описания'}"
    
class Sertificate(models.Model):
    CATEGORY_CHOICES = [
        ('fire_doors_cert', 'Сертификаты на противопожарные двери'),
        ('aluminum_structures_cert', 'Сертификаты на алюминиевые конструкции'),
        ('smoke_proof_doors_cert', 'Сертификаты на дымогазонепроницаемые двери'),
        ('product_cert', 'Сертификаты на изделия'),
        ('installation_license', 'Лицензия на осуществление монтажных работ'),
        ('certification_tests', 'Протоколы сертификационных испытаний'),
        ('gost_iso_cert', 'Сертификат соответствия требованиям ГОСТ Р ИСО'),
    ]
    photo = models.ImageField(upload_to="sertificates/")
    title = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(
        max_length=100, 
        choices=CATEGORY_CHOICES, 
        verbose_name="Категория"
    )
    class Meta:
        verbose_name="Сертификат"
        verbose_name_plural = "Сертификаты"
        
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('fire_doors', 'Противопожарные двери'),
        ('fire_hatches', 'Противопожарные люки'),
        ('fire_gates', 'Противопожарные ворота'),
        ('aluminum_structures', 'Алюминиевые конструкции'),
        ('hidden_doors', 'Скрытые двери'),
        ('ultra_clear_structures', 'Сверхпрозрачные конструкции'),
        ('technical_products', 'Технические изделия'),
    ]
    title = models.CharField(max_length=200, verbose_name="Название")
    price = models.IntegerField(verbose_name="Цена")
    photo = models.ImageField(upload_to="products/", verbose_name="Фото")
    category = models.CharField(
        max_length=50, 
        choices=CATEGORY_CHOICES, 
        verbose_name="Категория"
    )
    description = models.TextField(blank=True, verbose_name="Описание")
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        
    def __str__(self):
        return self.title