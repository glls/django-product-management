from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ["image_preview"]
    list_display = ["name", "category"]
    list_filter = ["name", "category"]
    search_fields = ["name", "category", "serial", "rfid", "code", "price"]

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src={} width="200" style="object-fit:contain;"/>', obj.image.url)
        return "(No image)"
    image_preview.short_description = "Current image"

    fields = ["name", "category", "notes", "serial", "rfid", "code", "image", "image_preview", "price"]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)