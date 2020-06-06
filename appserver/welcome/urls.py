from django.urls import path
from . import views

app_name = 'welcome'
urlpatterns = [
    path('', views.home, name='welcome'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
]