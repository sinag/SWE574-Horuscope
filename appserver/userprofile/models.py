from django.contrib.auth.models import User , AbstractUser
from django.db import models


class UserProfile(models.Model):
    #TODO: I was not able to get here from the
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    userName = "A Username that should come from django.contrib.auth.models"
    firstName = "Users First Name"
    dateJoined = "When the user is joined"
    def __str__(self):
        return self.username

    def __str__(self):
        return self.firstName

    def __str__(self):
        return self.dateJoined
