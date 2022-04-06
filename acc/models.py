from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    point = models.IntegerField(default=0)
    comment = models.TextField()
    pic = models.ImageField(upload_to="user/%y/%m")

    def getpic(self):
        if self.pic:
            return self.pic.url
        return "/media/noimage.jpeg"