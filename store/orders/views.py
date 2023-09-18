from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from orders.forms import OrderForm


class OrderCreateView(CreateView):
    template_name = 'orders/order-create.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:order_create')
    name_store = 'Оформление заказа'

    def form_valid(self, form):
        form.instance.initiators = self.request.user
        return super(OrderCreateView, self).form_valid(form=form)
