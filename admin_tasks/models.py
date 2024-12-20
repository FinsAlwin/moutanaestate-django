# admin_tasks/models.py

from django.db import models

from files_app.models import File


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Size(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Facing(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Shape(models.Model):
    name = models.CharField(
        max_length=100,
        help_text="Name or identifier for the shape",
        default="Unnamed Shape"
    )
    description = models.TextField(
        blank=True, help_text="Detailed description of the shape")
    shape_data = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    is_sold = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='shapes')
    facing = models.ForeignKey(
        Facing, on_delete=models.SET_NULL, null=True, blank=True)
    size = models.ForeignKey(
        Size, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
