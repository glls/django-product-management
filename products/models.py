from django.db import models
from django.contrib import admin

class Category(models.Model):
    name = models.CharField(max_length=100)
    #null & blank = allow top level categories without parent
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children') 

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    notes = models.TextField()
    serial = models.CharField(max_length=100, unique=True)
    rfid = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name