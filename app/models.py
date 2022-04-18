from __future__ import unicode_literals
from email.mime import image
from re import M
from tokenize import ContStr
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.conf import settings
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.urls import reverse


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

class menuItem(models.Model):
    name = models.CharField(max_length=100, null=False)
    cost = models.DecimalField(max_digits=6, decimal_places=2,null=False)
    description = models.CharField(max_length=400, null=False)
    image = models.ImageField(null=False)
    type = models.CharField(max_length=20)