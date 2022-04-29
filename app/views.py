from django.shortcuts import render, redirect
from django.template import context
from app.decorators import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib.auth.models import Group
from django.http import JsonResponse
import json
import datetime
from decimal import *

currentDate = datetime.datetime.now()
noOrdersButton = noOrdersModel.objects.get(id=1)

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
                return redirect('admin')
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
            group = Group.objects.get(name="user")
            user.groups.add(group)
            messages.success(request, 'Account was created for ' + username)
            new_cart = Cart(user=user)
            new_cart.save()
            return redirect('login')
    context = {'form':form}
    return render(request, 'signup.html', context)

@login_required(login_url='login')
def home(request):
    events = event.objects.all()
    context ={"events": events}
    return render(request,'index.html',context)

def paymentComplete(request):
    # if request.method == 'POST':
    cart = Cart.objects.get(user=request.user)
    cart.status = "paid"
    cart.save()
    body = json.loads(request.body)
    print("its hitting here")
        # print('BODY:', body)
        # return JsonResponse('Payment completed!', safe=False)
    return redirect('home ')

@login_required(login_url='login')
@admin_only
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
            newFood = AddToMenu(request.POST, request.FILES)
            if newFood.is_valid():
                newFood.save()
        elif request.POST.get("form_type") == "Event":
            createEvent = CreateEvent(request.POST)
            if createEvent.is_valid():
                createEvent.save()
    
    context = {'form': form, 'till': till, 'newFood': newFood,'createEvent': createEvent, 'noOrdersButton': noOrdersButton, 'paidOrders': Cart.objects.filter(status="paid")}
    return render(request,'admin.html',context)

def tillView(request):
    tills = closingTill.objects.all()
    context = {'tills': tills}
    return render(request, "till.html", context)

@admin_only
def deleteEvent(request):
    events = event.objects.all()
    events.delete()
    return redirect(request,'admin')

# RYLEE'S CODE

def sortMenu(request, type):
    return render(request, 'food.html', {'menu': menuItem.objects.filter(type=type)})

@admin_only
def turnOffOrders(request):
    form = CreateDailyLunch()
    till = CreateClosingTill()
    createEvent = CreateEvent()
    newFood = AddToMenu()
    if noOrdersButton.isActive == True:
        noOrdersButton.isActive = False
    else:
        noOrdersButton.isActive = True
    noOrdersButton.save()
    context = {'form': form, 'till': till, 'newFood': newFood,'createEvent': createEvent}
    return render(request,'admin.html',context)

def populateMenu(request):
    return render(request, "food.html",{"menu": checkDate(), "cartNum": cartItem.objects.all().count()})

def addToCart(request, itemname):
    itemFromMenu = menuItem.objects.get(name=itemname)
    cart = Cart.objects.get(user=request.user)
    new_cart_item = cartItem(cartItem.objects.all().count()+1,cost=itemFromMenu.cost,name=itemFromMenu.name, type=itemFromMenu.type)
    new_cart_item.save()
    new_cart_item.cart = cart
    new_cart_item.save()
    return render(request, 'food.html', {"menu": checkDate(), "cartNum": cartItem.objects.all().count()})

def removeFromCart(request, itemid):
    cartItem.objects.get(id=itemid).delete()
    cart = cartItem.objects.all()
    total = 0
    for item in cart:
        total += item.cost
    return render(request, 'cart.html', {"cart": cart, "total": total})

def checkDate() :
    if currentDate.weekday() != 4 and currentDate.weekday() != 5:
        menu = menuItem.objects.exclude(type="seafood")
    else: 
        menu = menuItem.objects.all()
    return menu

def cart(request) :
    cart = cartItem.objects.filter(cart=Cart.objects.get(user=request.user))
    total = 0
    for item in cart:
        total += item.cost
    totalTax = total + (total * Decimal(.07))
    return render(request, 'cart.html', {"cart": cart, "total": "{:.2f}".format(totalTax), "isActive": noOrdersButton})

def checkout(request) :
    cart = cartItem.objects.filter(cart=Cart.objects.get(user=request.user))
    userCart = Cart.objects.get(user=request.user)
    total = 0
    cartid = userCart.id
    for item in cart:
        total += item.cost
    totalTax = total + (total * Decimal(.07))
    print(cart)
    if request.method == "POST":
        cart = Cart.objects.get(user=request.user)
        cart.status = "paid"
        cart.save()
        return redirect('checkout')
    context = {"total":"{:.2f}".format(totalTax),"cartid":cartid,"userCart": userCart}
    return render(request, "checkout.html",context)

def itemPage(request, itemname):
    item = menuItem.objects.get(name=itemname)
    bigFood = createBig()
    smallFood = createSmall()
    food = createCartItem()
    cart = Cart.objects.get(user=request.user)
    if request.POST.get("form_type") == 'Add to Cart ':
        bigFood = createBig(request.POST)
        if bigFood.is_valid():
            new_cart_item = cartItem(cartItem.objects.all().count()+1,cost=item.cost,name=item.name, type=item.type,side1=bigFood.cleaned_data['side1'],side2=bigFood.cleaned_data['side2'],comment=bigFood.cleaned_data['comment'])
            new_cart_item.save()
            new_cart_item.cart = Cart.objects.get(user=request.user)
            new_cart_item.save()
            if new_cart_item.side1 == "Side Salad" or new_cart_item.side1 == "Loaded Baked Potato":
                new_cart_item.cost = new_cart_item.cost + Decimal(2.5)
                new_cart_item.save()
            if new_cart_item.side2 == "Side Salad" or new_cart_item.side2 == "Loaded Baked Potato":
                new_cart_item.cost = new_cart_item.cost + Decimal(2.5)
                new_cart_item.save()
            return render(request, 'food.html', {"menu": checkDate(), "cartNum": cartItem.objects.all().count(), "cart":cart})

    elif request.POST.get("form_type") == ' Add to Cart ':
        smallFood = createSmall(request.POST)
        if smallFood.is_valid(): 
            new_cart_item = cartItem(cartItem.objects.all().count()+1,cost=item.cost,name=item.name, type=item.type,side1=smallFood.cleaned_data['side1'],comment= smallFood.cleaned_data['comment'])
            new_cart_item.save()
            new_cart_item.cart = Cart.objects.get(user=request.user)
            new_cart_item.save()
            if new_cart_item.side1 == "side salad" or new_cart_item.side1 == "loaded baked potato":
                new_cart_item.cost = new_cart_item.cost + Decimal(2.5)
                new_cart_item.save()
            return render(request, 'food.html', {"menu": checkDate(), "cartNum": cartItem.objects.all().count(), "cart":cart})
    
    else:
        food = createCartItem(request.POST)
        if food.is_valid():
            new_cart_item = cartItem(cartItem.objects.all().count()+1,cost=item.cost,name=item.name, type=item.type,comment= food.cleaned_data['comment'])
            new_cart_item.save()
            new_cart_item.cart = Cart.objects.get(user=request.user)
            new_cart_item.save()
            return render(request, 'food.html', {"menu": checkDate(), "cartNum": cartItem.objects.all().count(), "cart":cart})
    return render(request, 'item.html', {"item": item, "cartNum": cartItem.objects.all().count(),"bigFood": bigFood,"smallFood":smallFood, "cart":cart})

def orderAdmin(request):
    carts = Cart.objects.filter(status="paid")
    context = {"carts": carts}
    return render(request, "orderadmin.html",context)

def finishOrder(request, cartId):
    cart = Cart.objects.get(id=cartId)
    cart.cartitem_set.all().delete()
    cart.status = 'unpaid'
    cart.save()
    return redirect('orderAdmin')