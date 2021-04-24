from django.shortcuts import render, redirect
from django.views import View
from store.models.order import Order
from store.models.product import Product
from store.models.customer import Customer


class Checkout(View):
    def post(self, request):
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        customer = request.session.get("customer")
        cart = request.session.get("cart")
        products = Product.get_product_by_id(list(cart.keys()))
        for p in products:
            instance = Order(
                customer = Customer(id=customer),
                product = p,
                quantity= cart.get(str(p.id)),
                price = p.price,
                address = address,
                phone= phone,
            )
            instance.save()
            request.session["cart"] = {}
        return redirect('/cart')