from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    Phone = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    @staticmethod
    def get_user_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
    def __str__(self):
        return self.first_name
