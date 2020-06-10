from django.urls import path
from . import views

app_name = 'city'
urlpatterns = [
    path( '<int:pk>/', views.search_city, name='city_search'),
]