from django.shortcuts import render, redirect
from app.decorators import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib.auth.models import Group
import datetime
from decimal import *


#important variables
currentDate = datetime.datetime.now()
noOrdersButton = noOrdersModel.objects.get(id=1)


# basic user login.  takes the normal user to the home page and the admin to our custom admin panel
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
    

# logs the user out
def logoutUser(request):
    logout(request)
    return redirect('login')


# user account creation.  also creates an empty cart for the user and redirects to the login
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
        else:
            print(form.errors.as_data())
    context = {'form':form}
    return render(request, 'signup.html', context)


# home page, displays the planned events
@login_required(login_url='login')
def home(request):          
    is_admin = request.user.groups.filter(name='admin').exists()
    events = event.objects.all()
    lunch = dailyLunch.objects.all()
    context ={"events": events,'is_admin': is_admin,"lunch": lunch}
    return render(request,'index.html',context)


# custom admin panel.  only for internal business use.
@login_required(login_url='login')
@admin_only
def admin(request):
    print(noOrdersButton.isActive)
    # grabbing empty forms
    form = CreateDailyLunch()
    till = CreateClosingTill()
    createEvent = CreateEvent()
    newFood = AddToMenu()
    if request.method == 'POST':
        #checks what form is used and submits/saves it
        if request.POST.get("form_type") == 'Daily Lunch':
            lunches = dailyLunch.objects.all()
            lunches.delete()
            form = CreateDailyLunch(request.POST)
            if form.is_valid():
                form.save()
        elif request.POST.get("form_type") == 'Till Out':
            till = CreateClosingTill(request.POST)
            if till.is_valid():
                till.save()
        elif request.POST.get("form_type") == 'Add New Menu Item':
            newFood = AddToMenu(request.POST, request.FILES)
            if newFood.is_valid():
                newFood.save()
        elif request.POST.get("form_type") == "Add an Event":
            events = event.objects.all()
            events.delete()
            createEvent = CreateEvent(request.POST)
            if createEvent.is_valid():
                createEvent.save()
    # puts all needed variables in context and returns to the page after the submit
    context = {'form': form, 'till': till, 'newFood': newFood,'createEvent': createEvent, 'noOrdersButton': noOrdersButton}
    return render(request,'admin.html',context)


# grabs the previous tills and renders the till page
def tillView(request):
    tills = closingTill.objects.all()
    context = {'tills': tills}
    return render(request, "till.html", context)


# deletes all events
@admin_only
def deleteEvent(request):
    events = event.objects.all()
    events.delete()
    return redirect('admin')


# toggles noOrdersButton.isActive.  Mrs. Coley can manually decide if she wants to stop taking online orders from the custom admin panel
@admin_only
def turnOffOrders(request):
    if noOrdersButton.isActive == True:
        noOrdersButton.isActive = False
    else:
        noOrdersButton.isActive = True
    noOrdersButton.save()
    return redirect('admin')


# Mrs Coley's view of the orders that have been paid.  She clicks a button that clears the cart once she is finished making the order
def orderAdmin(request):
    carts = Cart.objects.filter(status="paid")
    context = {"carts": carts}
    return render(request, "orderadmin.html",context)


# once Mrs Coley finishes making an order, she clicks a button that uses this view to clear out the user's cart so they can make another order
def finishOrder(request, cartId):
    cart = Cart.objects.get(id=cartId)
    cart.cartitem_set.all().delete()
    cart.status = 'unpaid'
    cart.save()
    return redirect('orderAdmin')


# populates menu, calls on the checkDate() function to see if it should include seafood or not
def populateMenu(request):
    return render(request, "food.html",{"menu": checkDate(), "cartNum": cartItem.objects.all().count()})


# seafood is only available on friday and saturday, so it checks the date to determine if its included or not
def checkDate() :
    if currentDate.weekday() != 4 and currentDate.weekday() != 5:
        menu = menuItem.objects.exclude(type="seafood")
    else: 
        menu = menuItem.objects.all()
    return menu

# displays the individual item, allows the user to pick sides if the food is a certain type, and allows for special comments on orders
def itemPage(request, itemname):
    item = menuItem.objects.get(name=itemname)
    bigFood = createBig()
    smallFood = createSmall()
    food = createCartItem()
    cart = Cart.objects.get(user=request.user)
# if the food is of type big then it gives two sides to be chosen
    if request.method == 'POST':
        if request.POST.get("form_type") == 'Add to Cart ':
            bigFood = createBig(request.POST)
            if bigFood.is_valid():
                new_cart_item = cartItem(cartItem.objects.all().count()+1,cost=item.cost,name=item.name, type=item.type,side1=bigFood.cleaned_data['side1'],side2=bigFood.cleaned_data['side2'],comment=bigFood.cleaned_data['comment'])
                new_cart_item.save()
                new_cart_item.cart = Cart.objects.get(user=request.user)
                new_cart_item.save()
                if new_cart_item.side1 == "side salad" or new_cart_item.side1 == "loaded baked potato":
                    new_cart_item.cost = new_cart_item.cost + Decimal(2.5)
                    new_cart_item.save()
                if new_cart_item.side2 == "side salad" or new_cart_item.side2 == "loaded baked potato":
                    new_cart_item.cost = new_cart_item.cost + Decimal(2.5)
                    new_cart_item.save()
                return render(request, 'food.html', {"menu": checkDate(), "cartNum": cartItem.objects.all().count(), "cart":cart})
# if the food is of type small then it gives one side to be chosen
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
# if the food has any other type it only gives a comment field
        else:
            food = createCartItem(request.POST)
            if food.is_valid():
                new_cart_item = cartItem(cartItem.objects.all().count()+1,cost=item.cost,name=item.name, type=item.type,comment=food.cleaned_data['comment'])
                new_cart_item.save()
                new_cart_item.cart = Cart.objects.get(user=request.user)
                new_cart_item.save()
                return render(request, 'food.html', {"menu": checkDate(), "cartNum": cartItem.objects.all().count(), "cart":cart})
    return render(request, 'item.html', {"item": item, "cartNum": cartItem.objects.all().count(),"bigFood": bigFood,"smallFood":smallFood, "food": food, "cart":cart})


# gets the users cart and removes the item
def removeFromCart(request, itemid):
    cartItem.objects.get(id=itemid).delete()
    cart = cartItem.objects.all()
    total = 0
    for item in cart:
        total += item.cost
    totalTax = (total * Decimal(.07))
    total = total + totalTax
    return render(request, 'cart.html', {"cart": cart, "total": "{:.2f}".format(total),"totalTax": "{:.2f}".format(totalTax)})


# gets the users cart and displays each item, as well as calculates the total with tax and see if the time is in range for online orders
def cart(request) :
    userCart = Cart.objects.get(user=request.user)
    # this if statement may cause problems later, we shall see
    if currentDate.weekday() != 4 and currentDate.weekday() != 5:
        for item in userCart.cartitem_set.all():
            if item.type == "seafood":
                userCart.objects.delete(id=item.id)
    cart = cartItem.objects.filter(cart=Cart.objects.get(user=request.user))
    total = 0
    for item in cart:
        total += item.cost
    totalTax = (total * Decimal(.07))
    total = total + totalTax
    if (currentDate.hour * 100 + currentDate.minute >= 130 and currentDate.hour < 19):
        storeHours = True
    else :
        storeHours = False
    if userCart.status == "paid":
        return render(request, 'paidTicket.html', {"totalTax": "{:.2f}".format(totalTax),"total": "{:.2f}".format(total), "cart": userCart})
    return render(request, 'cart.html', {"cart": cart,"total": "{:.2f}".format(total), "totalTax": "{:.2f}".format(totalTax), "isActive": noOrdersButton, "storeHours": storeHours})


# displays the total with tax and gives button options for payment.  Payment is handled through PayPal's code.  Cart status is changed to paid
def checkout(request) :
    cart = cartItem.objects.filter(cart=Cart.objects.get(user=request.user))
    userCart = Cart.objects.get(user=request.user)
    total = 0
    cartid = userCart.id
    for item in cart:
        total += item.cost
    totalTax = total + (total * Decimal(.07))
    if request.method == "POST":
        cart = Cart.objects.get(user=request.user)
        cart.status = "paid"
        cart.save()
        return redirect('checkout')
    context = {"total":"{:.2f}".format(totalTax), "cartid":cartid, "userCart": userCart}
    return render(request, "checkout.html", context)


# called by PayPal code, refreshes the page so that they are not prompted to pay twice, returns to home
def paymentComplete(request):
    cart = Cart.objects.get(user=request.user)
    cart.status = "paid"
    cart.save()
    return redirect('home')
