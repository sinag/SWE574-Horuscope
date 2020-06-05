from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import SignUpView, UpdateProfilePage, ViewProfilePage

app_name = 'users'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('view/<int:pk>/', ViewProfilePage.as_view(), name='view'),
    path('update/<int:pk>/', UpdateProfilePage.as_view(), name='update'),
]