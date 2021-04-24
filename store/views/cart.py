from django.shortcuts import render
from django.views import View
from store.models.product import Product


class Cart(View):
    def get(self, request):
        products = ''
        try:
            ids = list(request.session.get('cart').keys())
            if ids:
                products = Product.get_product_by_id(ids)
            return render(request, 'cart.html', {'products': products})
        except:
            return render(request, 'cart.html')
    

