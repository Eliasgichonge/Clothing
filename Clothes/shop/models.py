from django.db import models


class Product(models.Model):
      name = models.Charfield(max_length=100)
      price = models.DecimalField(max_digit=10, decimal_place=2)

