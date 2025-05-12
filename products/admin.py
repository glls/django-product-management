from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "category"]
    list_filter = ["name", "category"]
    search_fields = ["name", "category", "serial", "rfid", "code", "price"]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)