from django.shortcuts import render
from django.views import View
from store.models.order import Order

class OrderView(View):
    def get(self, request):
        customer = request.session.get("customer")
        orders = Order.get_order_by_customer(customer).order_by('date')
        return render(request, 'order.html', {'orders':orders})
