from django.db import models


class Product(models.Model):
      name = models.CharField(max_length=100)
      price = models.DecimalField(max_digit=10, decimal_place=2)
      image = models.ImageField(upload_to='products/')


      def __str__(self):

