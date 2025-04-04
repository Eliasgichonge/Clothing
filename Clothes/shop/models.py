2.	from django.db import models


4.	class Product(models.Model):
5.	    name = models.CharField(max_length=100)
6.	    price = models.DecimalField(max_digits=10, decimal_places=2)
7.	    image = models.ImageField(upload_to='products/')
8.
9.	    def __str__(self):
10.	        return self.name
