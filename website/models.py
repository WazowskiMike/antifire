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
    photo = models.ImageField(upload_to="sertificates/")
    title = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        verbose_name="Сертификат"
        verbose_name_plural = "Сертификаты"