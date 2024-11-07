# admin_tasks/serializers.py

from rest_framework import serializers
from .models import Shape, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at']


class ShapeSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source='category.name', read_only=True)
    size_display = serializers.CharField(
        source='get_size_display', read_only=True)

    class Meta:
        model = Shape
        fields = [
            'id', 'name', 'description', 'shape_data', 'created_at',
            'file', 'is_sold', 'facing', 'category', 'category_name',
            'size', 'size_display'
        ]
