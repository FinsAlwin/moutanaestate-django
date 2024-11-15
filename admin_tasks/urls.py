# admin_tasks/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('shapes/', views.ShapeListCreateAPIView.as_view(),
         name='shape-list-create'),
    path('shapes/<int:pk>/', views.ShapeDetailAPIView.as_view(), name='shape-detail'),
    path('categories/', views.CategoryListCreateAPIView.as_view(),
         name='category-list-create'),
    path('categories/<int:pk>/', views.CategoryDetailAPIView.as_view(),
         name='category-detail'),
    path('sizes/', views.SizeListCreateAPIView.as_view(), name='size-list'),
    path('sizes/<int:pk>/', views.SizeDetailAPIView.as_view(), name='size-detail'),
    path('facings/', views.FacingListCreateAPIView.as_view(), name='facing-list'),
    path('facings/<int:pk>/', views.FacingDetailAPIView.as_view(),
         name='facing-detail'),
    path('size-options/', views.SizeOptionsView.as_view(), name='size-options'),
    path('facing-options/', views.FacingOptionsView.as_view(), name='facing-options'),
]
