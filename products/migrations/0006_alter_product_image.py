# Generated by Django 5.2.1 on 2025-05-19 11:53

import products.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_category_options_alter_product_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', validators=[products.models.validate_image_file_size]),
        ),
    ]
