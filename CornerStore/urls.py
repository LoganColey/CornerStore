from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_page, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logoutUser, name="logout"),
    path('home/', views.home, name='home'),
    path('food/', views.populateMenu, name="food"),
    path('complete/', views.paymentComplete, name='complete'),
    path('adminpage/', views.admin, name='admin'),
    path('turnofforders/', views.turnOffOrders, name='turnOffOrders'),
    path('sortmenu/<type>/', views.sortMenu, name='sortmenu'),
    path('deleteEvent', views.deleteEvent, name="deleteEvent"),
    path('addtocart/<itemname>/', views.addToCart, name='addToCart'),
    path('tillView/', views.tillView, name='tillView')
]