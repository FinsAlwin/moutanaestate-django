# admin_tasks/views.py

from rest_framework import generics, permissions, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Shape, Category, Size, Facing
from .serializers import ShapeSerializer, CategorySerializer, SizeSerializer, FacingSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


class SizeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]


class SizeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    permission_classes = [permissions.IsAdminUser]


class FacingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Facing.objects.all()
    serializer_class = FacingSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]


class FacingDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Facing.objects.all()
    serializer_class = FacingSerializer
    permission_classes = [permissions.IsAdminUser]


class ShapeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Shape.objects.all()
    serializer_class = ShapeSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description',
                     'category__name', 'facing__name', 'size__name']
    ordering_fields = ['created_at', 'name', 'size__name']

    def get_authenticators(self):
        if self.request.method == 'GET':
            return []
        return [JWTAuthentication()]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]

    def get_queryset(self):
        queryset = super().get_queryset()

        category = self.request.query_params.get('category')
        if category:

            try:
                category_obj = Category.objects.get(id=category)
                if category_obj.name.lower() == 'common':

                    return Shape.objects.filter(category=category_obj)
            except Category.DoesNotExist:
                pass

        is_sold = self.request.query_params.get('is_sold')
        facing = self.request.query_params.get(
            'facing_id') or self.request.query_params.get('facing')
        size = self.request.query_params.get(
            'size_id') or self.request.query_params.get('size')

        if is_sold is not None:
            queryset = queryset.filter(is_sold=is_sold.lower() == 'true')
        if facing:
            queryset = queryset.filter(facing_id=facing)
        if category:
            queryset = queryset.filter(category_id=category)
        if size:
            queryset = queryset.filter(size_id=size)

        return queryset


class ShapeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shape.objects.all()
    serializer_class = ShapeSerializer

    permission_classes = [permissions.IsAdminUser]


class SizeOptionsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        sizes = Size.objects.all()
        return Response({
            'sizes': [
                {
                    'value': size.id,
                    'label': size.name,
                    'description': size.description
                } for size in sizes
            ]
        })


class FacingOptionsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        facings = Facing.objects.all()
        return Response({
            'facings': [
                {
                    'value': facing.id,
                    'label': facing.name,
                    'description': facing.description
                } for facing in facings
            ]
        })
