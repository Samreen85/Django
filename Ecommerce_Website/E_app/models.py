
# models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')  # Make sure Pillow is installed for image handling

    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import User

class User_Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  # Product name
    description = models.TextField()  # Product description
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Product price
    image = models.ImageField(upload_to='product_images/')  # Product image
    quantity = models.PositiveIntegerField(default=1)  # Quantity added

    class Meta:
        unique_together = ('user', 'name')  # Ensure one entry per product per user

    def __str__(self):
        return f"{self.user.username}'s cart: {self.name} x {self.quantity}"

