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