from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from user.models import CustomUser


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'username', 'password',
                  'is_active', 'phone', 'date_joined', 'last_login')
        extra_kwargs = {
            'date_joined': {'read_only': True},
            'last_login': {'read_only': True},
            'is_active': {'read_only': True},
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        instance = super().update(instance, validated_data)
        return instance


class CustomUserTokenSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }


class LoginResponseSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()
    user = CustomUserSerializer()


class CreateResponseSerializer(serializers.Serializer):
    detail = serializers.CharField()
    success = serializers.BooleanField()
    refresh = serializers.CharField()
    access = serializers.CharField()
    user = CustomUserSerializer()


class CreateUserResponseSerializer(serializers.Serializer):
    detail = serializers.CharField()
    success = serializers.BooleanField()
    refresh = serializers.CharField()
    access = serializers.CharField()
    user = CustomUserSerializer()


class ErrorResponseSerializer(serializers.Serializer):
    detail = serializers.CharField()
    success = serializers.BooleanField()
    data = serializers.DictField(child=serializers.CharField())


class ErrorResponseSerializer1(serializers.Serializer):
    detail = serializers.CharField()
    success = serializers.BooleanField()


