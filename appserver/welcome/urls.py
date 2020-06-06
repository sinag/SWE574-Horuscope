from django.urls import path
from . import views

app_name = 'welcome'
urlpatterns = [
    path('', views.home, name='welcome'),
    path('home/', views.home, name='home'),
]