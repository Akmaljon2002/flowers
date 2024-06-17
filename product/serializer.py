from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from product.models import Category, SubCategory, Product, Category2, Banner, ProductPhoto


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


class ProductPhotoSerializer(ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    product_photo = ProductPhotoSerializer(many=True, read_only=True)

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


class NarxSer(serializers.Serializer):
    dan = serializers.FloatField()
    gacha = serializers.FloatField()


class ProductsRequests(serializers.Serializer):
    narx = NarxSer(required=False)
    kesish = serializers.BooleanField(required=False)
    mahsulot_turi = serializers.ListField(child=serializers.CharField(max_length=100))
    rangi = serializers.ListField(child=serializers.CharField(max_length=100))
    qonish_joyi = serializers.ListField(child=serializers.CharField(max_length=100))
    gullash_oyi = serializers.ListField(child=serializers.CharField(max_length=100))
    shahar = serializers.ListField(child=serializers.CharField(max_length=100))
    sotib_olish_turi = serializers.ListField(child=serializers.CharField(max_length=100))

