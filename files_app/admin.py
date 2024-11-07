from django.contrib import admin
from .models import File


class FileAdmin(admin.ModelAdmin):
    list_display = ('user', 'file', 'uploaded_at')
    search_fields = ('user__username',)


admin.site.register(File, FileAdmin)
