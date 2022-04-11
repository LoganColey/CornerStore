from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.conf import settings

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.PROTECT, null=True)

class smallFood(models.Model):
    name = models.CharField(max_length=100, null=True) 
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    side = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=10000)
    image = models.ImageField(null=True)
    cart = models.ForeignKey(Cart,on_delete=models.PROTECT, null=True)

class bigFood(models.Model):
    name = models.CharField(max_length=100, null=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    side1 = models.CharField(max_length=100, null=True)
    side2 = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=10000)
    image = models.ImageField(null=True)
    cart = models.ForeignKey(Cart,on_delete=models.PROTECT, null=True)

class closingTill(models.Model):
    day = models.DateTimeField()
    month = models.DateTimeField()
    year = models.DateTimeField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    