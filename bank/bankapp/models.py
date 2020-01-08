from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    birth_date = models.DateField('Birth Date')

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.email

class Account(models.Model):
    balance = models.FloatField()
    type = models.CharField(max_length=10)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer.last_name + " " + self.type + ' ' + str(self.balance)