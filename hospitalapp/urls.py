
from django.contrib import admin
from django.urls import path
from hospitalapp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('service/', views.service, name='service'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('doctors/', views.doctors, name='doctors'),
    path('department/', views.department, name='department'),
    path('Appoint/', views.Appoint, name='Appoint'),
    path('contact/', views.contact, name='contact'),
]
