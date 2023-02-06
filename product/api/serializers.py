from rest_framework import serializers
from product.models import Category, Product
from product.api.selectors import category_list

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset = category_list(), source = "category", write_only=True
    )
    class Meta:
        model = Product
        fields = ['id', 'name', 'barcode', 'description', 'price', 'category', 'category_id', 'image']
