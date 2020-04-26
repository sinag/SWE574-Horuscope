"""root URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView, RedirectView

urlpatterns = [
    path('instance/', include('instance.urls')),
    path('properties/', include('property.urls')),
    path('subscriptions/', include('subscription.urls')),
    path('communities/', include('community.urls')),
    path('datatypes/', include('datatype.urls')),
    path('users/', include('users.urls')),
    path('flag/', include('flag.urls')),
    path('comment/', include('comment.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('userprofile/', include('userprofile.urls')),
    path('', RedirectView.as_view(pattern_name='community:index'))
]
