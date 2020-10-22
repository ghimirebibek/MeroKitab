from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
   path('', views.home, name='home'),
   path('signup/', views.signup_view, name='signup_view'),
   path('login/', views.login_view, name='login_view'),
   path('logout/', views.logoutUser, name='logout'),
   path('add_product/', views.addproduct, name='add_product'),
   path('edit_profile/',views.profile, name='profile'),
   path('contact/', views.contactus, name='contactus'),
   
]