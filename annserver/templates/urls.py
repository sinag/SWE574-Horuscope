from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from templates import views

urlpatterns = [
    # path('templates/', views.TemplateList.as_view()),
    # path('templates/<int:pk>/', views.TemplateDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

