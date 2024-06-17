from django.urls import path
from product.views import get_categories, get_products, get_banners, get_categories2, get_product

urlpatterns = [
    path('categories/', get_categories),
    path('categories2/', get_categories2),
    path('products/', get_products),
    path('product/detail/', get_product),
    path('banners/', get_banners),
]
