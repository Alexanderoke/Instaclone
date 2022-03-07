from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


images=[
  {
    'Image':'one',
    'comment':'is',
  },
  {
    'Image2':'two',
    'comment':'is',
  }

  ]




def home(request):
  context={
    'images':images
  }
  return render(request,'insta/home.html',context)


def register(request):
  return render(request,'insta/register.html')

def login(request):
  return render(request,'insta/login')
