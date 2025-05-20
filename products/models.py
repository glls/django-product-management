from django.db import models
from django.contrib import admin
from django.core.exceptions import ValidationError
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    #null & blank = allow top level categories without parent
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children') 

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

def validate_image_file_size(image):
    size_units = 1024 * 1024 # 1MB in bytes
    max_size = 20 * size_units  # 20MB max
    if image.size > max_size:
        raise ValidationError(f"Image size should not exceed {max_size / size_units:.2f}MB. Current size: {image.size / size_units:.2f}MB")
    return image

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    serial = models.CharField(max_length=100, unique=True)
    rfid = models.CharField(max_length=100, null=True, blank=True)
    code = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, validators=[validate_image_file_size])
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.image:
            self.image.open()  # Ensure file is open
            self.image.seek(0)  # Reset pointer to start
            img = Image.open(self.image)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            # Resize: largest side = 1024px, keep aspect ratio
            max_size = 1024
            width, height = img.size

            dimensions = {"width": width, "height": height}
            largest = max(dimensions, key=dimensions.get)

            #Reduce output dimensions if larger than max_size
            if dimensions[largest] > max_size:
                ratio = dimensions[largest] / max_size
                dimensions[largest] = max_size
                if largest != "width":
                    dimensions["width"] = int(dimensions["width"] / ratio)
                else:
                    dimensions["height"] = int(dimensions["height"] / ratio)
                img = img.resize((dimensions["width"], dimensions["height"]), Image.LANCZOS)

            # Compress to 85% quality 
            output = BytesIO()
            img.save(output, format='JPEG', quality=85)
            output.seek(0)
            self.image.save(
                f"{self.image.name.split('.')[0]}.jpg",
                ContentFile(output.read()),
                save=False # Don't save the model yet
            )
        super().save(*args, **kwargs) # Call the original save method to save the model
    
    def get_absolute_url(self):
        return reverse('product-detail-page', args=[str(self.id)])