from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product, Category, Banner, Category2
from product.schemas import get_category_schema, get_product_schema, get_banner_schema, get_category2_schema
from product.serializer import CategorySerializer1, ProductSerializer, BannerSerializer, Category2Serializer
from utils.pagination import paginate


@get_category_schema
@api_view(['GET'])
def get_categories(request):
    """
    Categoriyalar uchun get
    """
    categories = Category.objects.all().order_by('-id')
    serializer = CategorySerializer1(categories, many=True)
    return Response(serializer.data, status=200)


@get_product_schema
@api_view(['GET'])
def get_products(request):
    """
    Productlar uchun get
    """
    sub_id = request.query_params.get("subcategory_id")
    products = Product.objects.order_by('-id')
    if sub_id:
        products = products.filter(subcategory=sub_id)
    serializer = ProductSerializer(products.all(), many=True)
    return paginate(products.all(), ProductSerializer, request)


@get_banner_schema
@api_view(['GET'])
def get_banners(request):
    """
    Bannerlar uchun get
    """
    banners = Banner.objects.order_by('-id').all()
    serializer = BannerSerializer(banners, many=True)
    return Response(serializer.data, status=200)


@get_category2_schema
@api_view(['GET'])
def get_categories2(request):
    """
    Categoriyalar 2 uchun get
    """
    categories = Category2.objects.all().order_by('-id')
    serializer = Category2Serializer(categories, many=True)
    return Response(serializer.data, status=200)


