from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits = 10, decimal_places=2)
    inventory_quantity = models.IntegerField()
    image = models.CharField(max_length=255)
    