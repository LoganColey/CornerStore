from email.policy import default
from logging import PlaceHolder
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

class menuItem(models.Model):
    name = models.CharField(max_length=100, null=False)
    cost = models.DecimalField(max_digits=6, decimal_places=2,null=False)
    description = models.CharField(max_length=400, null=False)
    image = models.ImageField(null=True,blank=True,upload_to="images/")
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

class Cart(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=1000, null=True,default="unpaid")

class cartItem(models.Model): 
    SIDES = [('--Choose a Side--',
    (
    ('corn nuggets', 'Corn Nuggets'),
    ('tater tots', 'Tater Tots'),
    ('french fries', 'French Fries'),
    ('onion rings', 'Onion Rings'),
    ('fried okra', 'Fried Okra'),
    ('loaded baked potato', 'Loaded Baked Potato + $2.50'),
    ('side salad', 'Side Salad + $2.50'),
    ),)]
    id = models.IntegerField(null=False, primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    cost = models.DecimalField(default=0, decimal_places=2, max_digits=14)
    name = models.CharField(max_length=100, default="no name")
    type = models.CharField(max_length=20, default="no type")
    side1 = models.CharField(max_length=20,choices=SIDES, blank=False)
    side2 = models.CharField(max_length=20,choices=SIDES, blank=False)
    comment = models.CharField(max_length=1000, blank=True)