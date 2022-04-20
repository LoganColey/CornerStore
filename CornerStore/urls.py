from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_page, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logoutUser, name="logout"),
    path('home/', views.home, name='home'),
    path('food/', views.populateMenu, name="food"),
    path('checkout/', views.checkout, name="checkout"),
    path('complete/', views.paymentComplete, name='complete'),
    path('adminpage/', views.admin, name='admin')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)