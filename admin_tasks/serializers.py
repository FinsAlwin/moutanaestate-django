# admin_tasks/serializers.py

from rest_framework import serializers
from .models import Shape, Category, Size, Facing


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at']


class ShapeSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source='category.name', read_only=True)
    facing_name = serializers.CharField(
        source='facing.name', read_only=True)
    size_name = serializers.CharField(
        source='size.name', read_only=True)

    class Meta:
        model = Shape
        fields = [
            'id', 'name', 'description', 'shape_data', 'created_at',
            'file', 'is_sold', 'facing', 'category', 'category_name',
            'facing_name', 'size', 'size_name'
        ]


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'name', 'description', 'created_at']


class FacingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facing
        fields = ['id', 'name', 'description', 'created_at']
