from django.contrib import admin
from .models import Item

# Register your models here.
@admin.register(Item)
class ItemModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price', 'image','created_at', 'updated_at']