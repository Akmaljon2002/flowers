from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Product, Category
from product.schemas import get_current_user_schema
from product.serializer import CategorySerializer, CategorySerializer1


@get_current_user_schema
@api_view(['GET'])
def get_categories(request):
    """
    Categoriyalar uchun get
    """
    categories = Category.objects.all().order_by('-id')
    serializer = CategorySerializer1(categories, many=True)
    return Response(serializer.data, status=200)
