from django.contrib import admin

# Register your models here.

from .models import Avaliation, Category

admin.site.register(Avaliation)
admin.site.register(Category)