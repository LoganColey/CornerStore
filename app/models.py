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

class menuItem(models.Model):
    name = models.CharField(max_length=100, null=False)
    cost = models.DecimalField(max_digits=6, decimal_places=2,null=False)
    description = models.CharField(max_length=400, null=False)
    image = models.ImageField(null=True)
    type = models.CharField(max_length=20)

    def __str__(self) -> str:
           return self.name

class event(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=1000, null=False)
    day = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(31)])
    month = models.CharField(max_length=100, null=False)
    year  = models.IntegerField(validators=[MinValueValidator(2022),MaxValueValidator(2030)])

    def __str__(self) -> str:
           return self.name

class noOrdersModel(models.Model):
    isActive = models.BooleanField()
    
def create_isActive(isActive):
    noOrdersButton = noOrdersModel(isActive=isActive)
    noOrdersButton.save()
    return noOrdersButton