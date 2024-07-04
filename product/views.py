from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product, Category, Banner, Category2, AbouteProduct, Links, YoutubeVideo
from product.schemas import get_category_schema, get_product_schema, get_banner_schema, get_category2_schema, \
    get_product_detail_schema, get_aboute_product_schema, get_links_schema, get_youtube_schema
from product.serializer import CategorySerializer1, ProductSerializer, BannerSerializer, Category2Serializer, \
    ProductsRequests, AbouteProductSerializer, LinksSerializer, YoutubeSerializer
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
@api_view(['POST'])
def get_products(request):
    """
    Productlar uchun get
    """
    serializer = ProductsRequests(data=request.data)
    if serializer.is_valid():
        datas = serializer.data
        sub_id = request.query_params.get("subcategory_id")
        products = Product.objects.order_by('-id')
        if sub_id:
            products = products.filter(subcategory=sub_id)
        if datas["narx"]:
            products = products.filter(narx__gte=datas["narx"]['dan'], narx__lte=datas["narx"]['gacha'])
        if datas["kesish"]:
            products = products.filter(kesish=datas["kesish"])
        if datas["mahsulot_turi"]:
            products = products.filter(mahsulot_turi__in=datas["mahsulot_turi"])
        if datas["rangi"]:
            products = products.filter(rangi__in=datas["rangi"])
        if datas["qonish_joyi"]:
            products = products.filter(qonish_joyi__in=datas["qonish_joyi"])
        if datas["gullash_oyi"]:
            products = products.filter(gullash_davri__in=datas["gullash_oyi"])
        if datas["sotib_olish_turi"]:
            products = products.filter(sotib_olish_turi__in=datas["sotib_olish_turi"])
        if datas["shahar"]:
            products = products.filter(mamlakat__in=datas["shahar"])
        return paginate(products.all(), ProductSerializer, request)
    return Response(serializer.errors)


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


@get_product_detail_schema
@api_view(['GET'])
def get_product(request):
    """
    Productlar uchun get
    """
    pr_id = request.query_params.get("product_id")
    product = Product.objects.filter(id=pr_id).first()
    serializer = ProductSerializer(product)
    return Response(serializer.data, status=200)


@get_aboute_product_schema
@api_view(['GET'])
def get_aboute_product(request):
    """
    Gullar haqida
    """
    about_products = AbouteProduct.objects.order_by('-id').all()
    serializer = AbouteProductSerializer(about_products, many=True)
    return Response(serializer.data, status=200)


@get_links_schema
@api_view(['GET'])
def get_links(request):
    """
    Linklar
    """
    links = Links.objects.order_by('-id').all()
    serializer = LinksSerializer(links, many=True)
    return Response(serializer.data, status=200)


@get_youtube_schema
@api_view(['GET'])
def get_youtube(request):
    """
    Youtube Video uchun
    """
    link = YoutubeVideo.objects.order_by('-id').first()
    serializer = YoutubeSerializer(link)
    return Response(serializer.data, status=200)



