from django.urls import path
from flag.views import CreateView, DeleteView

app_name = 'flag'
urlpatterns = [
    path('create/<int:instance_id>', CreateView.as_view(), name='create'),
    path('delete/<int:pk>', DeleteView.as_view(), name='delete')
]
