from django.urls import path

from products.views import IndexView, ProductsView, basket_add, basket_remove

app_name = 'products'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('category/<int:category_id>/', ProductsView.as_view(), name='category'),
    path('page/<int:page>/', ProductsView.as_view(), name='paginator'),

    path('products/', ProductsView.as_view(), name='products'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
