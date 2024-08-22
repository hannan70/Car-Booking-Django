from django.shortcuts import render
from .models import Team
from cars.models import Car


# Create your views here.
def home_page(request):
    cars = Car.objects.all()
    context = {
        'cars': cars
    }
    return render(request, 'pages/home.html', context)


def about_page(request):
    return render(request, 'pages/about.html')


def service_page(request):
    return render(request, 'pages/service.html')


def contact_page(request):
    return render(request, 'pages/contact.html')
