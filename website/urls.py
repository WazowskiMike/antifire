from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('galery/', views.galery,name='galery'),
    path('delivery/', views.delivery,name='delivery'),
    path('sertificates/', views.sertificates,name='sertificates'),
    path('contacts/', views.contacts,name='contacts'),
    path('galery/<slug:slug>/', views.galery_detail, name='galery_detail'),
]