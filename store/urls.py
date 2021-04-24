from django.contrib import admin
from django.urls import path
from store.views.home import Home
from store.views.signup import SignUp
from store.views.login import Login, logout
from store.views.cart import Cart
from store.views.checkout import Checkout
from store.views.order import OrderView
# from store.middlewares.auth import auth_middleware

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('sign-up', SignUp.as_view(), name='sign-up'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    path('checkout', Checkout.as_view(), name='checkout'),
    path('order', OrderView.as_view(), name='order'),
    # path('order', auth_middleware(OrderView.as_view()), name='order'),
]