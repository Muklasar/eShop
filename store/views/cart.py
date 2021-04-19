from django.shortcuts import render
import django.views import views
import store.views.product import Product


class Cart(View):
    def get(self, request)
        return render(request, 'cart.html')
    