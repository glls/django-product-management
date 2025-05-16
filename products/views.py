from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
import qrcode
import qrcode.image.svg
from io import BytesIO

def home(request):
    return render(request, "products/home.html")

def product_list(request):
    products = Product.objects.all()
    return render(request, "products/product_list.html", {"products": products})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, "products/product_detail.html", {"product": product})

def generate_qr(request, url_path):
    # Full URL (adjust depending on your site settings)
    full_url = request.build_absolute_uri(url_path)

    # Use SVG image factory
    factory = qrcode.image.svg.SvgPathImage
    img = qrcode.make(full_url, image_factory=factory)

    stream = BytesIO()
    img.save(stream)
    svg_data = stream.getvalue()

    return HttpResponse(svg_data, content_type='image/svg+xml')