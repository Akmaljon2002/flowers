from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter

from product.serializer import CategorySerializer1, ProductSerializer, ProductsResponseModel, BannerSerializer, \
    Category2Serializer

get_category_schema = extend_schema(
    summary="Categoriyalar",
    responses=CategorySerializer1(many=True)
)


get_product_schema = extend_schema(
    summary="Products",
    request=None,
    responses=ProductsResponseModel(),
    parameters=[
        OpenApiParameter(name='subcategory_id', description='Subcategory id', required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name='limit', description='Page limit', required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name='offset', description='Page offset', required=False, type=OpenApiTypes.INT),
    ]
)


get_banner_schema = extend_schema(
    summary="Bannerlar",
    responses=BannerSerializer(many=True)
)


get_category2_schema = extend_schema(
    summary="Categoriyalar 2",
    responses=Category2Serializer(many=True)
)
