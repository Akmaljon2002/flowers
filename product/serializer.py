from rest_framework.serializers import ModelSerializer
from product.models import Category, SubCategory


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
