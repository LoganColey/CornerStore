from ast import Return
from django.shortcuts import render, redirect
from django.http import HttpRequest
from app.decorators import unauthenticated_user
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from typing import List
from dataclasses import dataclass
from .forms import *
from django.contrib.auth.models import Group
from json import dumps
from django.core import serializers

@unauthenticated_user
def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect.')
        context = {}
        return render(request, 'login.html', context)
    
def logoutUser(request):
    logout(request)
    return redirect('login')

@unauthenticated_user
def signup(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            cart = Cart()
            cart.user = user
            cart.save()

            group = Group.objects.get(name="user")
            user.groups.add(group)
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form':form}
    return render(request, 'signup.html', context)


def home(request):
    context ={}
    return render(request,'index.html',context)


def smallFoodOrder(request):
    cart = Cart.objects.get(user=request.user)
    form = CreatesmallFoodForm()
    if request.method == "POST":
        form = CreatesmallFoodForm(request.POST)
        if form.is_valid():
            if form.side == "Baked Potato" or form.side == "Loaded Fries":
                form.price += 1.50
            form.cart = cart
            form.save()
        context = {"form":form}
        return render(request,'food.html',context)

def bigFoodOrder(request):
    cart = Cart.objects.get(user=request.user)
    form = CreatebigFoodForm()
    if request.method == "POST":
        form = CreatebigFoodForm(request.POST)
        if form.is_valid():
            if form.side1 == "Baked Potato" or form.side1 == "Loaded Fries":
                form.price += 1.50
            if form.side2 == "Baked Potato" or form.side2 == "Loaded Fries":
                form.price += 1.50
            form.cart = cart
            form.save()
            
        context = {"form":form}
        return render(request,'food.html',context)

def food(request):
    cart = Cart.objects.get(user=request.user)
    form = CreatebigFoodForm()
    if request.method == "POST":
        form = CreatebigFoodForm(request.POST)
        if form.is_valid():
            if form.side1 == "Baked Potato" or form.side1 == "Loaded Fries":
                form.price += 1.50
            if form.side2 == "Baked Potato" or form.side2 == "Loaded Fries":
                form.price += 1.50
            form.cart = cart
            form.save()
            
    context = {"form":form}
    return render(request,'food.html',context)

def checkout(request):
    context ={}
    return render(request,'checkout.html',context)

def populateBigFood(request):
    return render(request, "food_mockup.html")
