from django.shortcuts import render
from .models import Team


# Create your views here.
def home_page(request):
    return render(request, 'pages/home.html')


def about_page(request):
    return render(request, 'pages/about.html')


def service_page(request):
    return render(request, 'pages/service.html')


def contact_page(request):
    return render(request, 'pages/contact.html')
