from xml.etree.ElementInclude import include
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import *
from django import forms

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

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class sideForm(ModelForm):
    class Meta:
        model = sideModel
        fields = ['side']
    side = forms.CharField(label='Choose a side', widget=forms.Select(choices=SIDES))
        

class createCartItem(ModelForm):
    class Meta:
        model = menuItem
        fields = ['name', 'cost', 'type']


class CreateDailyLunch(ModelForm):
    class Meta:
        model = dailyLunch
        fields = '__all__'

class CreateClosingTill(ModelForm):
    class Meta:
        model = closingTill
        fields = '__all__'

class AddToMenu(ModelForm):
    class Meta:
        model = menuItem
        fields = ['name', 'cost','description','type']

class CreateEvent(ModelForm):
    class Meta:
        model = event
        fields = '__all__'