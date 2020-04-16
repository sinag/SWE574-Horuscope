from django.urls import path
from subscription.views import CreateView, DeleteView

app_name = 'subscription'
urlpatterns = [
    path('create/<int:pk>', CreateView.as_view(), name='create'),
    path('delete/<int:pk>', DeleteView.as_view(), name='delete'),
]