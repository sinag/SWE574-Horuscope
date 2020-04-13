from django.urls import path

from community.views import CreateView, DeleteView, UpdateView
from . import views

app_name = 'community'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.PostsView.as_view(), name='posts'),
    path('delete/<int:pk>', DeleteView.as_view(), name='delete'),
    path('update/<int:pk>', UpdateView.as_view(), name='update'),
    path('create', CreateView.as_view(), name='create'),
]