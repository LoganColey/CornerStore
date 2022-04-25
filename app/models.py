from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

class closingTill(models.Model):
    date = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(max_digits=6, decimal_places=2)

class dailyLunch(models.Model):
    entree1 = models.CharField(max_length=100, null=True)
    entree2 = models.CharField(max_length=100, null=True)
    side1 = models.CharField(max_length=100, null=True)
    side2 = models.CharField(max_length=100, null=True)
    side3 = models.CharField(max_length=100, null=True)
    bread = models.CharField(max_length=100, null=True)
    dessert = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
           return self.name

class event(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=1000, null=False)

    def __str__(self) -> str:
           return self.name

class noOrdersModel(models.Model):
    isActive = models.BooleanField()

def create_isActive(isActive):
    noOrdersButton = noOrdersModel(isActive=isActive)
    noOrdersButton.save()
    return noOrdersButton

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.PROTECT, null=True)
    cost = models.DecimalField(max_digits=100,decimal_places=2,null=True)

class menuItem(models.Model):
    name = models.CharField(max_length=100, null=False)
    cost = models.DecimalField(max_digits=50, decimal_places=2,null=False)
    description = models.CharField(max_length=400, null=False)
    image = models.ImageField(null=True)
    type = models.CharField(max_length=20)

class cartItem(models.Model):
    name = models.CharField(max_length=100,null=False)
    cost = models.DecimalField(max_digits=50, null=False,decimal_places=2)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)