from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('expiry/', views.expiry_create, name='expiry'),
    path('qr/', views.qr_create, name='qr'),
    path('password/', views.password_create, name='password'),
    path('<str:pk>/', views.go, name='go'),
]