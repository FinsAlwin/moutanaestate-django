from django.db import models
from django.conf import settings
import os


class File(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return os.path.basename(self.file.name)

    @property
    def file_url(self):
        return self.file.url

    def delete(self, *args, **kwargs):
        # Delete the file from storage
        if self.file:
            if os.path.isfile(self.file.path):  # Check if the file exists
                # Remove the file from the filesystem
                os.remove(self.file.path)
        super().delete(*args, **kwargs)  # Call the superclass's delete method
