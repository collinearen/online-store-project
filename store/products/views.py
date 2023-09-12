from django.shortcuts import render


def index(request):
    context = {
        'name_store': "Coffee Lake"}
    return render(request=request, template_name="products/index.html", context=context)


def products(request):
    return render(request=request, template_name='products/products.html')
