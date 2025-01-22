from django.shortcuts import get_object_or_404, render
from .models import Blog
from .models import Gallery, Sertificate

def index(request):
    certificates = Sertificate.objects.all()
    return render(request, "index.html", {'certificates': certificates})

def galery(request):
    blogs = Blog.objects.all()
    galery = Gallery.objects.all()[0]
    context = {
        'blogs': blogs,
        'galery': galery,
    }
    return render(request, 'galery.html', context)

def delivery(request):
    return render(request, 'delivery.html')

def sertificates(request):
    sertificates = Sertificate.objects.all()
    context = {
        'sertificates': sertificates,
    }
    
    return render(request, 'sertificates.html', context)

def contacts(request):
    return render(request, 'contacts.html')

def galery_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    photos = blog.photos.all()
    return render(request, 'galery_detail.html', {'blog': blog, 'photos': photos})