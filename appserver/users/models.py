from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    user_name = models.CharField(max_length=30,blank=False)
    email = models.EmailField(max_length=254, blank=False)
    bio = models.CharField(max_length=500, blank=True)
    profile_pic = models.URLField(max_length=2000, blank=True)

    def __str__(self):
        return self.user_name
