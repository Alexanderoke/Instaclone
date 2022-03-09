from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
  image = models.ImageField()
  caption =models.TextField()
  author =models.ForeignKey(User, on_delete=models.CASCADE)
