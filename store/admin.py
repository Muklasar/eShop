from django.contrib import admin
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from store.models.order import Order


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)