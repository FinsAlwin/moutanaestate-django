# auth_app/urls.py

from django.urls import path
from .views import RegisterAPIView, LoginAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),  # JWT Token Obtain
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),    # JWT Token Refresh
]
