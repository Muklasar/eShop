from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password

def home_view(request):
    product = Product.objects.all()
    category = Category.objects.all()
    category_id = request.GET.get('category')
    if category_id:
        product = Product.get_product_by_category(category_id)
    data = {}
    data['product'] = product
    data['category'] = category
    return render(request, 'home.html', data)


def sign_in(request):
    errMsg = ''
    if request.method == "POST":
        data = request.POST
        email = data.get('email')
        password = data.get('password')
        value = {
            'email': email,
        }

        user = Customer.get_user_by_email(email=email)
        if user:
            if check_password(password, user.password):
                print("user login")
                return redirect('/')
            else:
                errMsg = "Password not match !"
                value["errMsg"] = errMsg
            return render(request, 'sign-in.html', value)
        else:
            errMsg = "Invalid Email"
            value["errMsg"] = errMsg
            return render(request, 'sign-in.html', value)
    return render(request, 'sign-in.html')

