from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    notes = models.TextField()
    serial = models.CharField(max_length=100, unique=True)
    rfid = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')
    price = models.DecimalField(max_digits=10, decimal_places=2)