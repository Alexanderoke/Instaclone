from django.urls import path
from . import views
from users import views as user_views


urlpatterns = [
  path('', user_views.login, name='users-login'),
  # path('register/',views.register, name='insta-register'),
  path('home/',views.home, name='insta-home'),
  
  
  
  
]