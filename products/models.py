from django.db import models
from django.contrib import admin
from django.core.exceptions import ValidationError

class Category(models.Model):
    name = models.CharField(max_length=100)
    #null & blank = allow top level categories without parent
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children') 

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

def validate_image_file_size(image):
    max_size = 100 * 1024  # 100kB max in bytes
    if image.size > max_size:
        raise ValidationError(f"Image size should not exceed {max_size / 1024:.2f}kB. Current size: {image.size / 1024:.2f}kB")
    return image

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    serial = models.CharField(max_length=100, unique=True)
    rfid = models.CharField(max_length=100, null=True, blank=True)
    code = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='media', null=True, blank=True, validators=[validate_image_file_size])
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name