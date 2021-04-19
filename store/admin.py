from django.contrib import admin
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)