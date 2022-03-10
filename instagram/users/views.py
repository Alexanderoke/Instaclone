from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm


# Create your views here.

def register(request):
  if request.method =='POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      form.save()
      username =form.cleaned_data.get('username')
      messages.success(request, f'Account successfully created for {username}! You can now Log in')
      return redirect('users-login')
  else:
    form =UserRegisterForm()  
  return render(request,'users/register.html',{'form':form})



def login(request):
  return render(request,'users/login.html')



def profile(request):
  return render(request, 'users/profile.html')

