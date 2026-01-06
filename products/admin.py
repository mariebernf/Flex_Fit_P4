from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


list_display = ('name',)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'size', 'gender', 'stock_quantity', 'is_active')
    list_filter = ('category', 'gender', 'size', 'is_active')
    search_fields = ('name', 'description')
