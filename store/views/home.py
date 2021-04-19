from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View

class Home(View):
    def get(self, request):
        product = Product.objects.all()
        category = Category.objects.all()
        category_id = request.GET.get('category')
        if category_id:
        #     request.session["category_id"] = category_id
        # c_id = request.session.get("category_id")
        # if c_id == '0':
        #     product = Product.objects.all()
        # else:
            product = Product.get_product_by_category(category_id)
        data = {}
        data['product'] = product
        data['category'] = category
        return render(request, 'home.html', data)

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')

        if cart:
            quantity = cart.get(product)
            qty_remove = cart.get(remove)
            if quantity:
                cart[product] = quantity + 1
            elif qty_remove:
                if qty_remove <=1:
                    cart.pop(remove)
                else:
                    cart[remove] = qty_remove - 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print(request.session["cart"])
        return redirect('/')