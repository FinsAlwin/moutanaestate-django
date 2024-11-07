from django.urls import path
from .views import FileUploadAPIView, FileListAPIView

urlpatterns = [
    path('upload/', FileUploadAPIView.as_view(), name='file-upload'),
    path('list-files/', FileListAPIView.as_view(), name='list-files'),
]
