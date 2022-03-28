from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_page, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logoutUser, name="logout"),
    path('home/', views.home, name='home'),
    path('food/', views.food, name="food"),
    path('cart/', views.checkout, name="checkout"),
    path('mockup/', views.mockup, name="mock")
]
