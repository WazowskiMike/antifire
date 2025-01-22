from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('galery/', views.galery,name='galery'),
    path('delivery/', views.delivery,name='delivery'),
    path('sertificates/', views.sertificates,name='sertificates'),
    path('contacts/', views.contacts,name='contacts'),
    path('galery/<slug:slug>/', views.galery_detail, name='galery_detail'),
    path('filter-products/', views.filter_products, name='filter_products'),
    path('filter-sertificates/', views.filter_sertificates, name='filter_sertificates'),
]