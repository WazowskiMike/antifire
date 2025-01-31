from django.shortcuts import get_object_or_404, render
from .models import Blog
from .models import Gallery, Sertificate, Product
from django.http import JsonResponse
from django.utils.html import escape
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = 'mail.nes-agency.ru'
SMTP_PORT = 465 
SMTP_USER = 'antifire@nes-agency.ru'
SMTP_PASSWORD = 'AntiFire'

# Настройки письма
from_email = SMTP_USER
to_email = 'ustanovkadverei.msk@yandex.ru'


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
            'description': escape(product.description),  # Экранирование HTML
            'photo': product.photo.url
        }
        for product in products
    ]

    return JsonResponse({'products': products_data}, safe=False)


def index(request):
    certificates = Sertificate.objects.all()
    products = Product.objects.all()
    if request.method == "POST":
            name = request.POST.get('name')
            telephone = request.POST.get('phone')
            subject =f"Новый клиент"
            body = f"Новый клиент!\n\nИмя: {name}\nТелефон: {telephone}"
            
            try:
                server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) 
                server.login(SMTP_USER, SMTP_PASSWORD)
                message = MIMEMultipart()
                message['From'] = from_email
                message['To'] = to_email
                message['Subject'] = subject
                message.attach(MIMEText(body, 'plain'))
                server.sendmail(from_email, to_email, message.as_string())
            except Exception as e:
                print(f"Ошибка отправки почты: {e}")
    return render(request, "index.html", {'certificates': certificates, 'products':products})

def galery(request):
    blogs = Blog.objects.all().order_by('-created_at')
    galery = Gallery.objects.all()[0]
    context = {
        'blogs': blogs,
        'galery': galery,
    }
    if request.method == "POST":
            name = request.POST.get('name')
            telephone = request.POST.get('phone')
            subject =f"Новый клиент"
            body = f"Новый клиент!\n\nИмя: {name}\nТелефон: {telephone}"
            
            try:
                server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) 
                server.login(SMTP_USER, SMTP_PASSWORD)
                message = MIMEMultipart()
                message['From'] = from_email
                message['To'] = to_email
                message['Subject'] = subject
                message.attach(MIMEText(body, 'plain'))
                server.sendmail(from_email, to_email, message.as_string())
            except Exception as e:
                print(f"Ошибка отправки почты: {e}")
    return render(request, 'galery.html', context)

def delivery(request):
    if request.method == "POST":
            name = request.POST.get('name')
            telephone = request.POST.get('phone')
            subject =f"Новый клиент"
            body = f"Новый клиент!\n\nИмя: {name}\nТелефон: {telephone}"
            
            try:
                server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) 
                server.login(SMTP_USER, SMTP_PASSWORD)
                message = MIMEMultipart()
                message['From'] = from_email
                message['To'] = to_email
                message['Subject'] = subject
                message.attach(MIMEText(body, 'plain'))
                server.sendmail(from_email, to_email, message.as_string())
            except Exception as e:
                print(f"Ошибка отправки почты: {e}")
    return render(request, 'delivery.html')

def sertificates(request):
    if request.method == "POST":
            name = request.POST.get('name')
            telephone = request.POST.get('phone')
            subject =f"Новый клиент"
            body = f"Новый клиент!\n\nИмя: {name}\nТелефон: {telephone}"
            
            try:
                server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) 
                server.login(SMTP_USER, SMTP_PASSWORD)
                message = MIMEMultipart()
                message['From'] = from_email
                message['To'] = to_email
                message['Subject'] = subject
                message.attach(MIMEText(body, 'plain'))
                server.sendmail(from_email, to_email, message.as_string())
            except Exception as e:
                print(f"Ошибка отправки почты: {e}")
    sertificates = Sertificate.objects.all()
    context = {
        'sertificates': sertificates,
    }
    
    return render(request, 'sertificates.html', context)

def contacts(request):
    if request.method == "POST":
            name = request.POST.get('name')
            telephone = request.POST.get('phone')
            subject =f"Новый клиент"
            body = f"Новый клиент!\n\nИмя: {name}\nТелефон: {telephone}"
            
            try:
                server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) 
                server.login(SMTP_USER, SMTP_PASSWORD)
                message = MIMEMultipart()
                message['From'] = from_email
                message['To'] = to_email
                message['Subject'] = subject
                message.attach(MIMEText(body, 'plain'))
                server.sendmail(from_email, to_email, message.as_string())
            except Exception as e:
                print(f"Ошибка отправки почты: {e}")
    return render(request, 'contacts.html')

def galery_detail(request, slug):
    if request.method == "POST":
            name = request.POST.get('name')
            telephone = request.POST.get('phone')
            subject =f"Новый клиент"
            body = f"Новый клиент!\n\nИмя: {name}\nТелефон: {telephone}"
            
            try:
                server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) 
                server.login(SMTP_USER, SMTP_PASSWORD)
                message = MIMEMultipart()
                message['From'] = from_email
                message['To'] = to_email
                message['Subject'] = subject
                message.attach(MIMEText(body, 'plain'))
                server.sendmail(from_email, to_email, message.as_string())
            except Exception as e:
                print(f"Ошибка отправки почты: {e}")
    blog = get_object_or_404(Blog, slug=slug)
    photos = blog.photos.all()
    return render(request, 'galery_detail.html', {'blog': blog, 'photos': photos})