from django.shortcuts import render, redirect
from django.views import View
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        errMsg = ''
        data = self.request.POST
        email = data.get('email')
        password = data.get('password')
        value = {
            'email': email,
        }

        customer = Customer.get_user_by_email(email=email)
        if customer:
            if check_password(password, customer.password):
                request.session["customer"] = customer.id
                return redirect('/')
            else:
                errMsg = "Password not match !"
                value["errMsg"] = errMsg
            return render(request, 'login.html', value)
        else:
            errMsg = "Invalid Email"
            value["errMsg"] = errMsg
            return render(request, 'login.html', value)


def logout(request):
    request.session.clear()
    return redirect('/')