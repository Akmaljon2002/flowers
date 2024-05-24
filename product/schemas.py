from drf_spectacular.utils import extend_schema

from product.serializer import CategorySerializer1

get_current_user_schema = extend_schema(
    summary="Categoriyalar",
    responses=CategorySerializer1
)
