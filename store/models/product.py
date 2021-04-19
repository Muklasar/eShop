from django.db import models
from .category import Category

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product')
    description = models.TextField()
    price = models.IntegerField()

    @staticmethod
    def get_all_product():
        return Product.objects.all()

    @staticmethod
    def get_product_by_category(category_id):
        return Product.objects.filter(category=category_id)

    def __str__(self):
        return self.name
    