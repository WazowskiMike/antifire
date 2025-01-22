from django.contrib import admin
from .models import Blog, BlogPhoto
from .models import Gallery, GalleryPhoto, Sertificate, Product

class BlogPhotoInline(admin.TabularInline):
    model = BlogPhoto
    extra = 1
    fields = ("photo", "caption")
    verbose_name = "Фотография"
    verbose_name_plural = "Фотографии"

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ("title", "created_at", "updated_at")
    inlines = [BlogPhotoInline]

class GalleryPhotoInline(admin.TabularInline):
    model = GalleryPhoto
    extra = 1
    fields = ("photo", "caption")
    verbose_name = "Фотография"
    verbose_name_plural = "Фотографии"

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [GalleryPhotoInline]
    
@admin.register(Sertificate)
class SertificateAdmin(admin.ModelAdmin):
    list_display = ("title", "photo")
    
admin.site.register(Blog, BlogAdmin)
admin.site.register(Product)