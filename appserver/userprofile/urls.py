from django.urls import path
from .views import CreateView
from . import views

app_name = 'userprofile'

urlpatterns = [
    path('profile/<int:username>', CreateView.as_view(), name='profile_page'),
]