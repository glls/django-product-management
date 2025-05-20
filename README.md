# Django Product Management System

## Overview

This project is a Django application for managing products with RFID tracking capabilities. It includes a comprehensive data model, an admin interface, and a RESTful API using Django REST Framework (DRF).

## Project Specifications

### Models

The core model of this application is `Product` with the following fields:

- `name`: Product name
- `notes`: Additional information about the product
- `serial`: Unique serial number
- `rfid`: RFID tag identifier
- `code`: Product code (SKU)
- `image`: Product image
- `price`: Product price

### Features

- Django Admin interface for product management
- RESTful API using Django REST Framework
- Image upload and management
- Search and filtering capabilities

## Learning Objectives

This project is designed as an exercise for new developers/students to learn:

1. Django model creation and management
2. Django Admin customization
3. REST API implementation with DRF
4. File upload handling in Django
5. Authentication and permissions

## Setup Instructions

### Prerequisites

- Python 3.10+ or higher
- pip package manager
- Django 5.2+
- DRF 3.16+

### Installation

1. Clone this repository:
```
git clone https://github.com/glls/django-product-management.git
cd django-product-management
```

2. Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Run migrations:
```
python manage.py migrate
```

5. Create a superuser for admin access:
```
python manage.py createsuperuser
```

6. Start the development server:
```
python manage.py runserver
```

## Project Structure

```
django-product-management/
├── product_management/       # Main Django project
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── products/                 # Products app
│   ├── migrations/
│   ├── models.py             # Contains Product model
│   ├── admin.py              # Admin interface configuration
│   ├── serializers.py        # DRF serializers
│   ├── views.py              # DRF API views
│   ├── urls.py               # API URL routing
│   └── tests.py              # Unit tests
├── media/                    # Uploaded images
├── static/                   # Static files
├── templates/                # HTML templates
├── manage.py
├── requirements.txt
└── README.md
```

## Exercise Tasks

### Task 1: Set Up the Project

- Initialize the Django project
- Create the products app
- Configure settings.py

### Task 2: Create the Product Model

- Implement the Product model with all required fields
- Create and apply migrations

### Task 3: Customize the Admin Interface

- Register the Product model with the admin site
- Add 'Category' model (name. parent) and property to 'Product' - should support hierarchy tree (parent child relationship)
- Customize the admin interface with list_display, search_fields, etc.
- Add filtering capabilities

### Task 4: Implement Django REST Framework

- Create serializers for the Product model
- Implement ViewSets or APIViews
- Configure URL routing for the API
- Add pagination

### Task 5: Add Authentication and Permissions

- Configure DRF authentication
- Set up appropriate permissions for API endpoints

### Task 6: Implement Image Upload

- Configure media settings
- Handle image upload in both admin and API
- Add product image restriction to 20MB
- Compress the product image file to max 1024px (on large size) and keep aspect-ratio
- Add basic product views with templates.
- Add qrcode link for each product.
- Add API authorization with API key.
To authorize add Authorization header to your http request as follows:
key: Authorization
value: Api-key <your-api-key>
- Add ordering in models by 'id' for consistent API views.

### Task 7: Write Tests

- Create unit tests for models
- Add API tests

## Bonus Challenges

- Add product categories and implement relationships between models
- Create a frontend using Django templates or a JavaScript framework
- Implement a barcode/QR code generator for products
- Add export functionality (CSV, PDF)
- Migrate from sqlite to PostgreSQL server

## Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework Documentation](https://www.django-rest-framework.org/)
- [Django File Uploads Documentation](https://docs.djangoproject.com/en/stable/topics/http/file-uploads/)
