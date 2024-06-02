from drf_spectacular.utils import extend_schema
from user.serializers import CustomUserSerializer, CustomUserTokenSerializer, LoginResponseSerializer, \
    CreateResponseSerializer, CreateUserResponseSerializer, ErrorResponseSerializer, ErrorResponseSerializer1
from utils.responses import response_schema

get_current_user_schema = extend_schema(
    summary="Get current user",
    responses=CustomUserSerializer
)

update_custom_user_schema = extend_schema(
    summary="Update current user",
    request=CustomUserSerializer,
    responses=response_schema
)


create_custom_user_schema = extend_schema(
    summary="Create new user",
    request=CustomUserSerializer,
    responses={
        201: CreateUserResponseSerializer,
        400: ErrorResponseSerializer
    }
)


login_custom_user_schema = extend_schema(
    summary="Login current user",
    request=CustomUserTokenSerializer,
    responses={200: LoginResponseSerializer, 404: ErrorResponseSerializer1}
)