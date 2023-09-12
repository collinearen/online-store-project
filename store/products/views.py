from django.shortcuts import render

from products.models import Product, ProductCategory


def index(request):
    return render(request=request, template_name="products/index.html")


def products(request):
    context = {
        'name_store': "Coffee Lake",
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request=request, template_name='products/products.html', context=context)
