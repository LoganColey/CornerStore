from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreatesmallFoodForm(ModelForm):
    class Meta:
        model = smallFood
        fields = ['name', 'cost', 'description', 'image']

class CreatebigFoodForm(ModelForm):
    class Meta:
        model = bigFood
        fields = ['name', 'cost' , 'description', 'image']

class CreateCart(ModelForm):
    class Meta:
        model = Cart
        fields = ['user']