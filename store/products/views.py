from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect

from products.models import Product, ProductCategory, Basket


def index(request):
    return render(request=request, template_name="products/index.html")


def products(request):
    context = {
        'name_store': "Coffee Lake",
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request=request, template_name='products/products.html', context=context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        baskets = baskets.first()
        baskets.quantity += 1
        baskets.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
