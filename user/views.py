from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from user.schemas import *
from user.serializers import CustomUserSerializer
from utils.responses import success

from user.schemas import update_custom_user_schema, get_current_user_schema


@get_current_user_schema
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_user(request):
    serializer = CustomUserSerializer(request.user)
    return Response(serializer.data, status=200)


@update_custom_user_schema
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_custom_user(request):
    serializer = CustomUserSerializer(request.user, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return success


@create_custom_user_schema
@api_view(['POST'])
def create_custom_user(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(is_active=True)
        user = authenticate(username=serializer.validated_data['username'],
                            password=serializer.validated_data['password'])
        refresh = RefreshToken.for_user(user)
        serialized_user = CustomUserSerializer(user).data
        return Response({'detail': 'Created successfully!',
                         'success': True,
                         'refresh': str(refresh),
                         'access': str(refresh.access_token),
                         'user': serialized_user}, status=201)
    return Response({'detail': 'Bad Request!',
                     'success': False,
                     'data': serializer.errors}, status=400)
