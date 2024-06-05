from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from product.models import Category, SubCategory, Product, Category2, Banner


class SubCategorySerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ["id", "name", "photo"]


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        category_id = data.get('id')
        subcategories = SubCategory.objects.filter(category__id=category_id).all()
        s_serializer = SubCategorySerializer(subcategories, many=True)
        data['subcategory'] = s_serializer.data
        return data


class CategorySerializer1(ModelSerializer):
    subcategory = SubCategorySerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = ["id", "name", "subcategory"]


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductsResponseModel(serializers.Serializer):
    count = serializers.IntegerField()
    next = serializers.CharField()
    previous = serializers.CharField()
    results = ProductSerializer(many=True)


class Category2Serializer(ModelSerializer):
    subcategory = SubCategorySerializer(read_only=True, many=True)

    class Meta:
        model = Category2
        fields = ["id", "name", "about", "subcategory"]


class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"
