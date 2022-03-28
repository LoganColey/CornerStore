from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.conf import settings

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.PROTECT, null=True)

class smallFood(models.Model):
    name = models.CharField(max_length=10000)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    side = (
        ("Fries", "Fries"),
        ("Spicy Fries", "Spicy Fries"),
        ("Tater Babies", "Tater Babies"),
        ("Corn Nuggets", "Corn Nuggets"),
        ("Fried Mushrooms", "Fried Mushrooms"),
        ("Mashed Potatoes", "Mashed Potatoes"),
        ("Fried Okra", "Fried Okra"),
        ("Salad", "Salad"),
        ("Onion Rings", "Onion Rings"),
        ("Loaded Baked Potato", "Loaded Baked Potato"),
        ("Tater Tots", "Tater Tots")
    )
    description = models.CharField(max_length=10000)
    image = models.ImageField(null=True)
    cart = models.ForeignKey(Cart,on_delete=models.PROTECT, null=True)

class bigFood(models.Model):
    name = models.CharField(max_length=10000)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    side1 = (
        ("Fries", "Fries"),
        ("Spicy Fries", "Spicy Fries"),
        ("Tater Babies", "Tater Babies"),
        ("Corn Nuggets", "Corn Nuggets"),
        ("Fried Mushrooms", "Fried Mushrooms"),
        ("Mashed Potatoes", "Mashed Potatoes"),
        ("Fried Okra", "Fried Okra"),
        ("Salad", "Salad"),
        ("Onion Rings", "Onion Rings"),
        ("Loaded Baked Potato", "Loaded Baked Potato"),
        ("Tater Tots", "Tater Tots")
    )
    side2 = (
        ("Fries", "Fries"),
        ("Spicy Fries", "Spicy Fries"),
        ("Tater Babies", "Tater Babies"),
        ("Corn Nuggets", "Corn Nuggets"),
        ("Fried Mushrooms", "Fried Mushrooms"),
        ("Mashed Potatoes", "Mashed Potatoes"),
        ("Fried Okra", "Fried Okra"),
        ("Salad", "Salad"),
        ("Onion Rings", "Onion Rings"),
        ("Loaded Baked Potato", "Loaded Baked Potato"),
        ("Tater Tots", "Tater Tots")
    )
    description = models.CharField(max_length=10000)
    image = models.ImageField(null=True)
    cart = models.ForeignKey(Cart,on_delete=models.PROTECT, null=True)


