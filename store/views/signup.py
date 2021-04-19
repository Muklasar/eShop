from django.views import View
from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password


class SignUp(View):
    def get(self, request):
        return render(request, 'sign-up.html')

    def post(self, request):
        data = self.request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        phone = data.get('phone')
        password = data.get('password')
        value = {'first_name': first_name, 'last_name': last_name, 'email': email, 'phone':phone}

        customer = Customer(
                        first_name=first_name, 
                        last_name=last_name, 
                        email=email, 
                        Phone=phone, 
                        password=password,
                    )
        errMsg = self.validateCustomer(customer)
        if errMsg:
            data= {
            'errMsg': errMsg,
            'values' : value 
        }
            return render(request, 'sign-up.html', data)
        else:
            customer.password = make_password(password) 
            customer.save()
            return redirect('/')

    def validateCustomer(self, customer):
        errMsg = ""
        verify_email = Customer.objects.filter(email=customer.email).exists()
        verify_phone = Customer.objects.filter(Phone=customer.Phone).exists()
        if not customer.first_name:
                errMsg = 'First Name Required !'
        elif len(customer.first_name)<4:
            errMsg = 'First Name lenth should be 5 character !'
        elif not customer.last_name:
            errMsg = 'Last Name Required!'
        elif verify_email:
            errMsg = 'Email is already exists !'
        elif not customer.Phone:
            errMsg = 'Phone Number Required !'
        elif len(customer.Phone) < 10:
            errMsg = 'Phone should be 10 digits !'
        elif verify_phone:
            errMsg = 'Phone is already exists !'
        elif not customer.password:
            errMsg = 'Password Requred !'
        elif len(customer.password)<6:
            errMsg = 'Password length must be 6 !'
        return errMsg   

