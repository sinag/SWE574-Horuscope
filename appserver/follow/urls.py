from django.urls import path
from follow.views import CreateView, DeleteView

app_name = 'follow'
urlpatterns = [
    path('create/<int:target_id>', CreateView.as_view(), name='create'),
    path('delete/<int:pk>', DeleteView.as_view(), name='delete')
]
