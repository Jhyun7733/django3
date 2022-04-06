from django.db import models
from acc.models import User
# Create your models here.

class Book(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    impo = models.BooleanField()
    site_name=models.CharField(max_length=200)
    site_url=models.TextField()
    site_con=models.TextField()

    def __str__(self):
        return self.site_name