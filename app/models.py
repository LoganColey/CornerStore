from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

SIDES = [('--Choose a Side--',
    (
    ('corn nuggets', 'Corn Nuggets'),
    ('tater tots', 'Tater Tots'),
    ('french fries', 'French Fries'),
    ('onion rings', 'Onion Rings'),
    ('fried okra', 'Fried Okra'),
    ('loaded baked potato', 'Loaded Baked Potato'),
    ('side salad', 'Side Salad'),
    ),)]

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
    date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
           return self.name
    
class noOrdersModel(models.Model):
    isActive = models.BooleanField()

    def __str__(self) -> str:
           return self.isActive

def create_isActive(isActive):
    noOrdersButton = noOrdersModel(isActive=isActive)
    noOrdersButton.save()
    return noOrdersButton

class Cart(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)

def createCart(id, user):
    new_cart = Cart(id=id, user=user)
    new_cart.save()
    return new_cart

class cartItem(models.Model):
    id = models.IntegerField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    cost = models.DecimalField(default=0, decimal_places=2, max_digits=14)
    name = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=20, null=True)
    side1 = models.CharField(max_length=20, null=True)
    side2 = models.CharField(max_length=20, null=True)

def createCartItem(id, user, cost, name, type):
    new_cart = cartItem(id=id, user=user,name=name,cost=cost, type=type)
    new_cart.save()
    return new_cart

# class sideModel(models.Model):
#     SIDES = [('--Choose a Side--',
#     (
#     ('corn nuggets', 'Corn Nuggets'),
#     ('tater tots', 'Tater Tots'),
#     ('french fries', 'French Fries'),
#     ('onion rings', 'Onion Rings'),
#     ('fried okra', 'Fried Okra'),
#     ('loaded baked potato', 'Loaded Baked Potato'),
#     ('side salad', 'Side Salad'),
#     ),)]
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     cartItem = models.ForeignKey(menuItem, on_delete=models.CASCADE, null=True)
#     option = models.CharField(max_length=200, null=True,choices=SIDES)
