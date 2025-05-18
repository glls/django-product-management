from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product_list, name='product-list-page'),
    path('product/<int:pk>/', views.product_detail, name='product-detail-page'),
    path('qr<path:url_path>', views.generate_qr, name='generate_qr'),
]