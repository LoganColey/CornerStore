from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.conf import settings

class Food(models.Model):
    name = models.CharField(max_length=10000)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    sides = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)])
    description = models.CharField(max_length=10000)
    image = models.ImageField(null=True)

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.PROTECT, null=True)
    food = models.ForeignKey(Food,on_delete=models.PROTECT, null=True)
