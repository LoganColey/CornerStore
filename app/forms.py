from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import *
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class createCartItem(ModelForm):

    class Meta:
        model = cartItem
        fields = ['comment']

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
        fields = '__all__'

class CreateEvent(ModelForm):
    class Meta:
        model = event
        fields = '__all__'

class createBig(ModelForm):
    
    class Meta:
        model = cartItem
        fields = ['side1', 'side2', 'comment']

class createSmall(ModelForm):

    class Meta:
        model = cartItem
        fields = ['side1', 'comment']
