from django.contrib import admin
from django.urls import path
from store.views.home import Home
from store.views.signup import SignUp
from store.views.login import Login, logout

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('sign-up', SignUp.as_view(), name='sign-up'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
]