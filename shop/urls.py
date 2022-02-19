from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'), #ova dva koristimo u models.py fajlu kod funkcije get_absolute_url
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search_products', views.search_products, name='search-products'),
]
