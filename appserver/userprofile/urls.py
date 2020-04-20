from django.urls import path

from .views import UserView

app_name = 'userprofile'

urlpatterns = [
    path('', UserView.as_view(), name='profile_page')
]