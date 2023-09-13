from django.urls import path

from products.views import products, index

app_name = 'products'

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products'),
]
