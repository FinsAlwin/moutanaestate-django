# admin_tasks/views.py

from rest_framework import generics, permissions, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Shape, Category
from .serializers import ShapeSerializer, CategorySerializer


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


class ShapeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Shape.objects.all()
    serializer_class = ShapeSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description', 'category__name']
    ordering_fields = ['created_at', 'name', 'size']

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]

    def get_queryset(self):
        queryset = super().get_queryset()

        is_sold = self.request.query_params.get('is_sold')
        facing = self.request.query_params.get('facing')
        category = self.request.query_params.get('category')
        size = self.request.query_params.get('size')

        if is_sold is not None:
            queryset = queryset.filter(is_sold=is_sold.lower() == 'true')
        if facing:
            queryset = queryset.filter(facing__iexact=facing)
        if category:
            queryset = queryset.filter(category_id=category)
        if size:
            queryset = queryset.filter(size=size.upper())

        return queryset


class ShapeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shape.objects.all()
    serializer_class = ShapeSerializer

    permission_classes = [permissions.IsAdminUser]


class SizeChoicesView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response({
            'sizes': [
                {
                    'value': size[0],
                    'label': size[1]
                } for size in Shape.SIZE_CHOICES
            ]
        })
