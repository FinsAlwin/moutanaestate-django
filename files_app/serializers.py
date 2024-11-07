from rest_framework import serializers
from .models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'user', 'file', 'file_url', 'uploaded_at']
        read_only_fields = ['user', 'file_url', 'uploaded_at']
