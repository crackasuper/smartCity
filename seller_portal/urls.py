from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('add_product/', views.add_product, name='add_product'),
   # path('seller/', views.become_seller, name='seller'),
    path('seller/dashboard/', views.seller_dashboard, name='seller_dashboard'),
]