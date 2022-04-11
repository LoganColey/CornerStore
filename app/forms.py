from xml.etree.ElementInclude import include
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import *
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CreatesmallFoodForm(ModelForm):
    class Meta:
        model = smallFood
        fields ='__all__'
        exclude = ['cost']
        side = forms.CharField(label="pick a side", widget=forms.Select(choices=SIDES))

class CreatebigFoodForm(ModelForm):
    class Meta:
        model = bigFood
        fields ='__all__'
        exclude = ['cost']
        side1 = forms.CharField(label="pick a side", widget=forms.Select(choices=SIDES))
        side2 = forms.CharField(label="pick a side", widget=forms.Select(choices=SIDES))


class CreateCart(ModelForm):
    class Meta:
        model = Cart
        fields = ['user']

class CreateDailyLunch(ModelForm):
    class Meta:
        model = dailyLunch
        fields = '__all__'

class CreateClosingTill(ModelForm):
    class Meta:
        model = closingTill
        fields = '__all__'
