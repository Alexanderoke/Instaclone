from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
  image = models.ImageField(null = True, blank=True, upload_to = 'home_pics')
  caption =models.TextField()
  author =models.ForeignKey(User, on_delete=models.CASCADE)


  def __str__(self):
    return self.caption
