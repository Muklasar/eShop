from django.db import models
from .customer import Customer
from .product import Product
import datetime

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default="1")
    price = models.IntegerField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product} of {self.quantity}"

    def get_order_by_customer(customer):
        order = Order.objects.filter(customer=customer)
        return order

    
    
    
