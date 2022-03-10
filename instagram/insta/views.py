from django.shortcuts import render
from .models import Post
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
    'posts': Post.objects.all()
  }
  return render(request,'insta/home.html',context)




