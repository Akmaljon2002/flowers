from django.urls import path
from product.views import get_categories

urlpatterns = [
    path('categories/', get_categories)
]
