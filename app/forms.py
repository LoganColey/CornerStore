from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateFoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'cost', 'sides', 'description', 'image']

class CreateCartForm(ModelForm):
    class Meta:
        model = Cart
        fields = ['food']