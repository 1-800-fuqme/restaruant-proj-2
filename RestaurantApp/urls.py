"""
URL configuration for RestaurantApp app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('index/', views.index, name='index'),
    path('account/', views.account, name='account'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('cookbook/', views.cookbook, name='cookbook'),
    path('menu/', views.menu, name='menu'),
]
