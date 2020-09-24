from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:product_slug>/details/',
         views.product_page, name='product_detail'),
    path('<slug:product_slug>/purchase/',
         views.purchase_item, name='product_purchase'),
    path('search/', views.search, name='search'),
]
