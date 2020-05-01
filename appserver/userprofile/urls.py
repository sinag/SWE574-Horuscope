from django.urls import path
from .views import CreateView
from . import views

app_name = 'userprofile'

urlpatterns = [
    path('profile/', CreateView.as_view(), name='profile'),
]