from django.urls import path
from . import views

urlpatterns = [
  path('', views.login, name='insta-login'),
  path('register/',views.register, name='insta-register'),
  path('home/',views.home, name='insta-home'),
  
  
  
  
]