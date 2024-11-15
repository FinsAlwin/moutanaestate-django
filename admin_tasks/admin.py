from django.contrib import admin
from .models import Shape, Category, Size, Facing
# Register your models here.
admin.site.register(Shape)
admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Facing)
