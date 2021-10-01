from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source= 'created_by.username', read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'title')

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return Category.objects.create(**validated_data)


class BookSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.username', read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'category', 'isbn', 'pages', 'price',
                  'stock', 'description', 'imageUrl', 'status', 'date_created', 'created_by')

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return Book.objects.create(**validated_data)


class ProductSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.username', read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'product_tag', 'name', 'category',
                  'price', 'stock', 'imageUrl', 'status', 'date_created', 'created_by')

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return Product.objects.create(**validated_data)


