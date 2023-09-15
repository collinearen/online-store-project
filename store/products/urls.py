from django.urls import path

from products.views import products, index, basket_add, basket_remove

app_name = 'products'

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>/', products, name='category'),
    path('products/', products, name='products'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
