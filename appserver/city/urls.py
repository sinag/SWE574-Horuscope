from django.urls import path
from . import views

app_name = 'city'
urlpatterns = [
    path('', views.search_city, name='city_search'),
    path('city/', views.search_city, name='city_search'),
]