from django import forms
from .models import UserProfile

class UserPage(UserProfile):
    model = UserProfile
    fields = ('name','email')
    deneme = deneme