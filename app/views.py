from django.shortcuts import render, redirect
from app.decorators import unauthenticated_user
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib.auth.models import Group
from django.http import JsonResponse
import json 
noOrdersButton = create_isActive(False)

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
                with open('app/static/food.json', 'a') as f:
                    f.truncate(0)
                    f.write("[")
                    menu = menuItem.objects.all()
                    for item in menu:
                        f.write('{"name":"' + item.name + '", "cost":' + str(item.cost) +', "description": "' + item.description + '", "image":"none", "type": "' + item.type + '"}')
                        if item.id != menuItem.objects.all().last().id:
                            f.write(",")
                    f.write("]")
                    f.close
                newFood.save()
        elif request.POST.get("form_type") == "Event":
            createEvent = CreateEvent(request.POST)
            if createEvent.is_valid():
                createEvent.save()
    context = {'form': form, 'till': till, 'newFood': newFood,'createEvent': createEvent}
    return render(request,'admin.html',context)

def populateMenu(request):
    if noOrdersButton.isActive == True:
        return render(request, "noOrders.html")
    else:
        return render(request, "food.html")

def turnOffOrders(request):
    if noOrdersButton.isActive == True:
        noOrdersButton.isActive = False
    else:
        noOrdersButton.isActive = True
    noOrdersButton.save()
    print(noOrdersButton.isActive)
    return redirect('admin')