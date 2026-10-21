from django.db import models

# Create your models here.

from django.db import models

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    food_item = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.FloatField()
    is_delivered = models.BooleanField()
