from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Additional fields can be added here
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username
