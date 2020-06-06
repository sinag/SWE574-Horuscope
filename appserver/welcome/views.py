# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse


def home(request):
    if request.user.is_authenticated:
        return redirect('activitystream:index')
    else:
        return render(request, template_name='welcome/welcome.html')


def about(request):
    return render(request, template_name='welcome/welcome.html')
