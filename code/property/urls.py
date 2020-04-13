from django.urls import path

from property.views import CreateView, DeleteView
from . import views

app_name = 'property'
urlpatterns = [
    path('<int:datatype_id>', views.IndexView.as_view(), name='index'),
    path('create/<int:datatype_id>', CreateView.as_view(), name='create'),
    path('delete/<int:datatype_id>/<int:pk>', DeleteView.as_view(), name='delete'),
]
