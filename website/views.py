from django.shortcuts import get_object_or_404, render
from .models import Blog
from .models import Gallery, Sertificate, Product
from django.http import JsonResponse

def filter_sertificates(request):
    category = request.GET.get('category', None)
    if category:
        sertificates = Sertificate.objects.filter(category=category)
    else:
        sertificates = Sertificate.objects.all()

    sertificates_data = [
        {
            'photo': sert.photo.url,
            'title': sert.title,
        }
        for sert in sertificates
    ]
    return JsonResponse({'sertificates': sertificates_data})

def filter_products(request):
    category = request.GET.get('category', None)
    if category:
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()

    products_data = [
        {
            'title': product.title,
            'price': product.price,
            'photo': product.photo.url
        }
        for product in products
    ]
    return JsonResponse({'products': products_data})

def index(request):
    certificates = Sertificate.objects.all()
    products = Product.objects.all()
    return render(request, "index.html", {'certificates': certificates, 'products':products})

def galery(request):
    blogs = Blog.objects.all().order_by('-created_at')
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