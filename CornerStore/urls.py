from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
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
    # path('sortmenu/<type>/', views.sortMenu, name='sortmenu'),
    path('deleteEvent', views.deleteEvent, name="deleteEvent"),
    # path('addtocart/<itemname>/', views.addToCart, name='addToCart'),
    path('removefromcart/<itemid>/', views.removeFromCart, name='removeFromCart'),
    path('tillview', views.tillView,name='tillView'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('item/<itemname>/', views.itemPage, name="item"),
    path('viewOrders/', views.orderAdmin, name='orderAdmin'),
    path('finishOrder/<int:cartId>/', views.finishOrder, name='finishOrder')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)