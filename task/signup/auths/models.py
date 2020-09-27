from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Favourites(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    favourites = models.CharField(max_length=30, null =True)

    def __str__(self):
        return self.favourites