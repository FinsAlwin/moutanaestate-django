from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth_app.urls')),
    path('files/', include('files_app.urls')),
    path('admin-tasks/', include('admin_tasks.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
