from django.urls import path
from comment.views import CreateView, DeleteView, UpdateView
from . import views

app_name = 'comment'
urlpatterns = [
    path('<int:instance_id>/', views.CommentsView.as_view(), name='comments'),
    path('create/<int:instance_id>', CreateView.as_view(), name='create'),
    path('update/<int:pk>', UpdateView.as_view(), name='update'),
    path('delete/<int:pk>', DeleteView.as_view(), name='delete')
]
