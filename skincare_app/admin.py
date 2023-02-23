from django.contrib import admin
from skincare_app.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category')
    list_filter = ('brand', 'category')
    search_fields = ('name', 'brand', 'category')
