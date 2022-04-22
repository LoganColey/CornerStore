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
from django.http import JsonResponse
import json 
from django.core.files import File

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

@login_required(login_url='login')
def home(request):
    context ={}
    return render(request,'index.html',context)

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def checkout(request):
    cart = Cart.objects.get(user=request.user)
    foods = bigFood.objects.filter(cart=cart)
    price = 0
    for food in foods:
        food.price += price
    context = {"price":price}
    return render(request,'checkout.html',context)

def paymentComplete(request):
    body = json.loads(request.body)
    print('BODY:', body)
    return JsonResponse('Payment completed!', safe=False)

@login_required(login_url='login')
def admin(request):
    form = CreateDailyLunch()
    till = CreateClosingTill()
    createEvent = CreateEvent()
    newFood = AddToMenu()
    if request.method == 'POST':
        if request.POST.get("form_type") == 'Change Lunch':
            form = CreateDailyLunch(request.POST)
            if form.is_valid():
                form.save()
        elif request.POST.get("form_type") == 'Till Out':
            till = CreateClosingTill(request.POST)
            if till.is_valid():
                till.save()
        elif request.POST.get("form_type") == 'Add Item':
            newFood = AddToMenu(request.POST)
            if newFood.is_valid():
                newFood.save()
        elif request.POST.get("form_type") == "Event":
            createEvent = CreateEvent(request.POST)
            if createEvent.is_valid():
                createEvent.save()
    context = {'form': form, 'till': till, 'newFood': newFood,'createEvent': createEvent}
    return render(request,'admin.html',context)

def populateMenu(request):
    with open('app/static/food.json', 'a') as f:
        f.truncate(0)
        f.write("[")
        menu = menuItem.objects.all()
        for item in menu:
            f.write('{"name":"' + item.name + '", "cost":' + str(item.cost) +', "description": "' + item.description + '", "image":"none", "type": "' + item.type + '"}')
            if item.id != menuItem.objects.all().last().id:
              f.write(",")
            print(item.id)
        f.write("]")
        f.close
    return render(request, "food.html")
