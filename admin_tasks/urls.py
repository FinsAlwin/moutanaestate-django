# admin_tasks/urls.py

from django.urls import path
from .views import (
    ShapeListCreateAPIView,
    ShapeDetailAPIView,
    CategoryListCreateAPIView,
    CategoryDetailAPIView,
    SizeChoicesView
)

urlpatterns = [
    path('shapes/', ShapeListCreateAPIView.as_view(), name='shape-list-create'),
    path('shapes/<int:pk>/', ShapeDetailAPIView.as_view(), name='shape-detail'),
    path('categories/', CategoryListCreateAPIView.as_view(),
         name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(),
         name='category-detail'),
    path('sizes/', SizeChoicesView.as_view(), name='size-choices'),
]
